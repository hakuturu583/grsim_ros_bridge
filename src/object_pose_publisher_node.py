#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from grsim_ros_bridge.msg import FieldObjects

def callback(msg):
    for ball in msg.balls:
        ball_pose_msg = PoseStamped()
        ball_pose_msg.header.stamp = rospy.Time.now()
        ball_pose_msg.header.frame_id = msg.header.frame_id
        ball_pose_msg.pose.position = ball.point
        ball_pose_msg.pose.orientation.x = 0
        ball_pose_msg.pose.orientation.y = 0
        ball_pose_msg.pose.orientation.z = 0
        ball_pose_msg.pose.orientation.w = 1
        ball_pose_pub.publish(ball_pose_msg)
    for robot in msg.robots:
        if robot.team_color == robot.BLUE:
            robot_pose_msg = PoseStamped()
            robot_pose_msg.pose = robot.robot_pose
            robot_pose_msg.header.stamp = rospy.Time.now()
            robot_pose_msg.header.frame_id = msg.header.frame_id
            if robot.robot_id == 0:
                blue_robot_0_pose_pub.publish(robot_pose_msg)
            if robot.robot_id == 1:
                blue_robot_1_pose_pub.publish(robot_pose_msg)
            if robot.robot_id == 2:
                blue_robot_2_pose_pub.publish(robot_pose_msg)
            if robot.robot_id == 3:
                blue_robot_3_pose_pub.publish(robot_pose_msg)
            if robot.robot_id == 4:
                blue_robot_4_pose_pub.publish(robot_pose_msg)
            if robot.robot_id == 5:
                blue_robot_5_pose_pub.publish(robot_pose_msg)
        if robot.team_color == robot.YELLOW:
            robot_pose_msg = PoseStamped()
            robot_pose_msg.pose = robot.robot_pose
            robot_pose_msg.header.stamp = rospy.Time.now()
            robot_pose_msg.header.frame_id = msg.header.frame_id
            if robot.robot_id == 0:
                yellow_robot_0_pose_pub.publish(robot_pose_msg)
            if robot.robot_id == 1:
                yellow_robot_1_pose_pub.publish(robot_pose_msg)
            if robot.robot_id == 2:
                yellow_robot_2_pose_pub.publish(robot_pose_msg)
            if robot.robot_id == 3:
                yellow_robot_3_pose_pub.publish(robot_pose_msg)
            if robot.robot_id == 4:
                yellow_robot_4_pose_pub.publish(robot_pose_msg)
            if robot.robot_id == 5:
                yellow_robot_5_pose_pub.publish(robot_pose_msg)

if __name__ == '__main__':
    rospy.init_node('pose_publisher_node', anonymous=False)
    ball_pose_pub = rospy.Publisher('/ball/pose', PoseStamped, queue_size=1)
    blue_robot_0_pose_pub = rospy.Publisher('/blue/robot0/robot_pose', PoseStamped, queue_size=1)
    blue_robot_1_pose_pub = rospy.Publisher('/blue/robot1/robot_pose', PoseStamped, queue_size=1)
    blue_robot_2_pose_pub = rospy.Publisher('/blue/robot2/robot_pose', PoseStamped, queue_size=1)
    blue_robot_3_pose_pub = rospy.Publisher('/blue/robot3/robot_pose', PoseStamped, queue_size=1)
    blue_robot_4_pose_pub = rospy.Publisher('/blue/robot4/robot_pose', PoseStamped, queue_size=1)
    blue_robot_5_pose_pub = rospy.Publisher('/blue/robot5/robot_pose', PoseStamped, queue_size=1)
    yellow_robot_0_pose_pub = rospy.Publisher('/yellow/robot0/robot_pose', PoseStamped, queue_size=1)
    yellow_robot_1_pose_pub = rospy.Publisher('/yellow/robot1/robot_pose', PoseStamped, queue_size=1)
    yellow_robot_2_pose_pub = rospy.Publisher('/yellow/robot2/robot_pose', PoseStamped, queue_size=1)
    yellow_robot_3_pose_pub = rospy.Publisher('/yellow/robot3/robot_pose', PoseStamped, queue_size=1)
    yellow_robot_4_pose_pub = rospy.Publisher('/yellow/robot4/robot_pose', PoseStamped, queue_size=1)
    yellow_robot_5_pose_pub = rospy.Publisher('/yellow/robot5/robot_pose', PoseStamped, queue_size=1)
    rospy.Subscriber('/field_objects', FieldObjects, callback)
    rospy.spin()
