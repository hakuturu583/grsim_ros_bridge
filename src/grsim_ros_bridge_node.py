#!/usr/bin/env python
import  socket
import  messages_robocup_ssl_wrapper_pb2
import rospy
from geometry_msgs.msg import Quaternion,Vector3,TransformStamped
from grsim_ros_bridge.msg import FieldObjects,Ball,Robot
import math
import google
import tf
import tf2_ros

def euler_to_quaternion(euler):
    q = tf.transformations.quaternion_from_euler(euler.x, euler.y, euler.z)
    return Quaternion(x=q[0], y=q[1], z=q[2], w=q[3])

def broadcast_transform(broadcaster,robot_id,team_color,robot_x,robot_y,robot_thata):
    transform_stamped = TransformStamped()
    transform_stamped.header.stamp = rospy.Time.now()
    transform_stamped.header.frame_id = "map"
    transform_stamped.child_frame_id = "robot_" + team_color + "_" + str(robot_id) + "_frame"
    transform_stamped.transform.translation.x = robot_x
    transform_stamped.transform.translation.y = robot_y
    transform_stamped.transform.translation.z = 0.0
    q = tf.transformations.quaternion_from_euler(0, 0, robot_thata)
    transform_stamped.transform.rotation.x = q[0]
    transform_stamped.transform.rotation.y = q[1]
    transform_stamped.transform.rotation.z = q[2]
    transform_stamped.transform.rotation.w = q[3]
    broadcaster.sendTransform(transform_stamped)

def create_field_objects_message(data,broadcaster):
    msg = FieldObjects()
    msg.header.frame_id = "map"
    msg.header.stamp.secs = int(math.floor(float(data.detection.t_capture)))
    msg.header.stamp.nsecs = int((float(data.detection.t_capture)-math.floor(float(data.detection.t_capture)))*pow(10,9))
    msg.time_sent.secs = int(math.floor(float(data.detection.t_sent)))
    msg.time_sent.nsecs = int((float(data.detection.t_sent)-math.floor(float(data.detection.t_sent)))*pow(10,9))
    msg.camera_id = int(data.detection.camera_id)
    for ball in data.detection.balls:
        ball_msg = Ball()
        ball_msg.confidence = ball.confidence
        ball_msg.point.x = float(ball.x)/1000
        ball_msg.point.y = float(ball.y)/1000
        ball_msg.point.z = float(ball.z)/1000
        ball_msg.pixel_x = float(ball.pixel_x)
        ball_msg.pixel_y = float(ball.pixel_y)
        msg.balls.append(ball_msg)
    for robot in data.detection.robots_blue:
        robot_msg = Robot()
        robot_msg.team_color = robot_msg.BLUE
        robot_msg.robot_id = int(robot.robot_id)
        robot_msg.confidence = float(robot.confidence)
        robot_msg.robot_pose.position.x = float(robot.x)/1000
        robot_msg.robot_pose.position.y = float(robot.y)/1000
        robot_msg.robot_pose.position.z = 0
        quat = euler_to_quaternion(Vector3(0.0, 0.0, float(robot.orientation)))
        robot_msg.robot_pose.orientation.x = quat.x
        robot_msg.robot_pose.orientation.y = quat.y
        robot_msg.robot_pose.orientation.z = quat.z
        robot_msg.robot_pose.orientation.w = quat.w
        broadcast_transform(broadcaster,int(robot.robot_id),"blue",float(robot.x)/1000,float(robot.y)/1000,float(robot.orientation))
        msg.robots.append(robot_msg)
    for robot in data.detection.robots_yellow:
        robot_msg = Robot()
        robot_msg.team_color = robot_msg.YELLOW
        robot_msg.robot_id = int(robot.robot_id)
        robot_msg.confidence = float(robot.confidence)
        robot_msg.robot_pose.position.x = float(robot.x)/1000
        robot_msg.robot_pose.position.y = float(robot.y)/1000
        robot_msg.robot_pose.position.z = 0
        quat = euler_to_quaternion(Vector3(0.0, 0.0, float(robot.orientation)))
        robot_msg.robot_pose.orientation.x = quat.x
        robot_msg.robot_pose.orientation.y = quat.y
        robot_msg.robot_pose.orientation.z = quat.z
        robot_msg.robot_pose.orientation.w = quat.w
        broadcast_transform(broadcaster,int(robot.robot_id),"yellow",float(robot.x)/1000,float(robot.y)/1000,float(robot.orientation))
        msg.robots.append(robot_msg)
    return msg

if __name__ == '__main__':
    rospy.init_node('grsim_ros_bridge', anonymous=False)
    multicast_if_addr='192.168.3.9'
    multicast_group='224.5.23.2'
    multicast_port=10020
    my_addr='0.0.0.0'
    server_address=(my_addr, multicast_port)
    sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(server_address)
    mreq=socket.inet_aton(multicast_group)+socket.inet_aton(multicast_if_addr)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    #make protobuf instance
    ssl_wrapper = messages_robocup_ssl_wrapper_pb2.SSL_WrapperPacket()
    #make publisher
    field_objects_pub = rospy.Publisher('/field_objects', FieldObjects, queue_size=1)
    field_objects_msg = FieldObjects()
    broadcaster = tf2_ros.TransformBroadcaster()
    while not rospy.is_shutdown():
        data = sock.recv(1024)
        try:
            ssl_wrapper.ParseFromString(data)
            field_objects_msg = create_field_objects_message(ssl_wrapper,broadcaster)
            field_objects_pub.publish(field_objects_msg)
        except google.protobuf.message.DecodeError:
            pass
        except:
            import traceback
            traceback.print_exc()
