#!/usr/bin/env python
import rospy
from visualization_msgs.msg import Marker
from geometry_msgs.msg import PoseStamped

class marker_publisher:
    def __init__(self):
        self.ball_marker_pub = rospy.Publisher('/ball/marker', Marker, queue_size=1)
        self.blue_robot_0_marker_pub = rospy.Publisher('/blue/robot0/marker', Marker, queue_size=1)
        self.blue_robot_1_marker_pub = rospy.Publisher('/blue/robot1/marker', Marker, queue_size=1)
        self.blue_robot_2_marker_pub = rospy.Publisher('/blue/robot2/marker', Marker, queue_size=1)
        self.blue_robot_3_marker_pub = rospy.Publisher('/blue/robot3/marker', Marker, queue_size=1)
        self.blue_robot_4_marker_pub = rospy.Publisher('/blue/robot4/marker', Marker, queue_size=1)
        self.blue_robot_5_marker_pub = rospy.Publisher('/blue/robot5/marker', Marker, queue_size=1)
        self.yellow_robot_0_marker_pub = rospy.Publisher('/yellow/robot0/marker', Marker, queue_size=1)
        self.yellow_robot_1_marker_pub = rospy.Publisher('/yellow/robot1/marker', Marker, queue_size=1)
        self.yellow_robot_2_marker_pub = rospy.Publisher('/yellow/robot2/marker', Marker, queue_size=1)
        self.yellow_robot_3_marker_pub = rospy.Publisher('/yellow/robot3/marker', Marker, queue_size=1)
        self.yellow_robot_4_marker_pub = rospy.Publisher('/yellow/robot4/marker', Marker, queue_size=1)
        self.yellow_robot_5_marker_pub = rospy.Publisher('/yellow/robot5/marker', Marker, queue_size=1)

        self.ball_marker_sub = rospy.Subscriber('/ball/pose', PoseStamped, self.callback_ball)
        self.blue_robot_0_pose_sub = rospy.Subscriber('/blue/robot0/robot_pose', PoseStamped, self.callback_blue_robot_0_pose)
        self.blue_robot_1_pose_sub = rospy.Subscriber('/blue/robot1/robot_pose', PoseStamped, self.callback_blue_robot_1_pose)
        self.blue_robot_2_pose_sub = rospy.Subscriber('/blue/robot2/robot_pose', PoseStamped, self.callback_blue_robot_2_pose)
        self.blue_robot_3_pose_sub = rospy.Subscriber('/blue/robot3/robot_pose', PoseStamped, self.callback_blue_robot_3_pose)
        self.blue_robot_4_pose_sub = rospy.Subscriber('/blue/robot4/robot_pose', PoseStamped, self.callback_blue_robot_4_pose)
        self.blue_robot_5_pose_sub = rospy.Subscriber('/blue/robot5/robot_pose', PoseStamped, self.callback_blue_robot_5_pose)
        self.yellow_robot_0_pose_sub = rospy.Subscriber('/yellow/robot0/robot_pose', PoseStamped, self.callback_yellow_robot_0_pose)
        self.yellow_robot_1_pose_sub = rospy.Subscriber('/yellow/robot1/robot_pose', PoseStamped, self.callback_yellow_robot_1_pose)
        self.yellow_robot_2_pose_sub = rospy.Subscriber('/yellow/robot2/robot_pose', PoseStamped, self.callback_yellow_robot_2_pose)
        self.yellow_robot_3_pose_sub = rospy.Subscriber('/yellow/robot3/robot_pose', PoseStamped, self.callback_yellow_robot_3_pose)
        self.yellow_robot_4_pose_sub = rospy.Subscriber('/yellow/robot4/robot_pose', PoseStamped, self.callback_yellow_robot_4_pose)
        self.yellow_robot_5_pose_sub = rospy.Subscriber('/yellow/robot5/robot_pose', PoseStamped, self.callback_yellow_robot_5_pose)

    #publish ball marker
    def callback_ball(self,msg):
        marker_msg = Marker()
        marker_msg.header = msg.header
        marker_msg.type = marker_msg.SPHERE
        marker_msg.action = marker_msg.ADD
        marker_msg.pose = msg.pose
        marker_msg.scale.x = 0.1
        marker_msg.scale.y = 0.1
        marker_msg.scale.z = 0.1
        marker_msg.color.r = 1
        marker_msg.color.g = 1
        marker_msg.color.b = 0
        marker_msg.color.a = 1
        self.ball_marker_pub.publish(marker_msg)

    #publish blue robot marker
    def callback_blue_robot_0_pose(self,msg):
        marker_msg = Marker()
        marker_msg.header = msg.header
        marker_msg.type = marker_msg.MESH_RESOURCE
        marker_msg.action = marker_msg.ADD
        marker_msg.pose = msg.pose
        marker_msg.scale.x = 1
        marker_msg.scale.y = 1
        marker_msg.scale.z = 1
        marker_msg.frame_locked = True
        marker_msg.mesh_use_embedded_materials = True
        marker_msg.mesh_resource = "package://grsim_ros_bridge/resources/robot_marker_blue.dae"
        self.blue_robot_0_marker_pub.publish(marker_msg)

    #publish blue robot marker
    def callback_blue_robot_1_pose(self,msg):
        marker_msg = Marker()
        marker_msg.header = msg.header
        marker_msg.type = marker_msg.MESH_RESOURCE
        marker_msg.action = marker_msg.ADD
        marker_msg.pose = msg.pose
        marker_msg.scale.x = 1
        marker_msg.scale.y = 1
        marker_msg.scale.z = 1
        marker_msg.frame_locked = True
        marker_msg.mesh_use_embedded_materials = True
        marker_msg.mesh_resource = "package://grsim_ros_bridge/resources/robot_marker_blue.dae"
        self.blue_robot_1_marker_pub.publish(marker_msg)

    #publish blue robot marker
    def callback_blue_robot_2_pose(self,msg):
        marker_msg = Marker()
        marker_msg.header = msg.header
        marker_msg.type = marker_msg.MESH_RESOURCE
        marker_msg.action = marker_msg.ADD
        marker_msg.pose = msg.pose
        marker_msg.scale.x = 1
        marker_msg.scale.y = 1
        marker_msg.scale.z = 1
        marker_msg.frame_locked = True
        marker_msg.mesh_use_embedded_materials = True
        marker_msg.mesh_resource = "package://grsim_ros_bridge/resources/robot_marker_blue.dae"
        self.blue_robot_2_marker_pub.publish(marker_msg)

    #publish blue robot marker
    def callback_blue_robot_3_pose(self,msg):
        marker_msg = Marker()
        marker_msg.header = msg.header
        marker_msg.type = marker_msg.MESH_RESOURCE
        marker_msg.action = marker_msg.ADD
        marker_msg.pose = msg.pose
        marker_msg.scale.x = 1
        marker_msg.scale.y = 1
        marker_msg.scale.z = 1
        marker_msg.frame_locked = True
        marker_msg.mesh_use_embedded_materials = True
        marker_msg.mesh_resource = "package://grsim_ros_bridge/resources/robot_marker_blue.dae"
        self.blue_robot_3_marker_pub.publish(marker_msg)

    #publish blue robot marker
    def callback_blue_robot_4_pose(self,msg):
        marker_msg = Marker()
        marker_msg.header = msg.header
        marker_msg.type = marker_msg.MESH_RESOURCE
        marker_msg.action = marker_msg.ADD
        marker_msg.pose = msg.pose
        marker_msg.scale.x = 1
        marker_msg.scale.y = 1
        marker_msg.scale.z = 1
        marker_msg.frame_locked = True
        marker_msg.mesh_use_embedded_materials = True
        marker_msg.mesh_resource = "package://grsim_ros_bridge/resources/robot_marker_blue.dae"
        self.blue_robot_4_marker_pub.publish(marker_msg)

    #publish blue robot marker
    def callback_blue_robot_5_pose(self,msg):
        marker_msg = Marker()
        marker_msg.header = msg.header
        marker_msg.type = marker_msg.MESH_RESOURCE
        marker_msg.action = marker_msg.ADD
        marker_msg.pose = msg.pose
        marker_msg.scale.x = 1
        marker_msg.scale.y = 1
        marker_msg.scale.z = 1
        marker_msg.frame_locked = True
        marker_msg.mesh_use_embedded_materials = True
        marker_msg.mesh_resource = "package://grsim_ros_bridge/resources/robot_marker_blue.dae"
        self.blue_robot_5_marker_pub.publish(marker_msg)

    #publish yellow robot marker
    def callback_yellow_robot_0_pose(self,msg):
        marker_msg = Marker()
        marker_msg.header = msg.header
        marker_msg.type = marker_msg.MESH_RESOURCE
        marker_msg.action = marker_msg.ADD
        marker_msg.pose = msg.pose
        marker_msg.scale.x = 1
        marker_msg.scale.y = 1
        marker_msg.scale.z = 1
        marker_msg.frame_locked = True
        marker_msg.mesh_use_embedded_materials = True
        marker_msg.mesh_resource = "package://grsim_ros_bridge/resources/robot_marker_yellow.dae"
        self.yellow_robot_0_marker_pub.publish(marker_msg)

    #publish yellow robot marker
    def callback_yellow_robot_1_pose(self,msg):
        marker_msg = Marker()
        marker_msg.header = msg.header
        marker_msg.type = marker_msg.MESH_RESOURCE
        marker_msg.action = marker_msg.ADD
        marker_msg.pose = msg.pose
        marker_msg.scale.x = 1
        marker_msg.scale.y = 1
        marker_msg.scale.z = 1
        marker_msg.frame_locked = True
        marker_msg.mesh_use_embedded_materials = True
        marker_msg.mesh_resource = "package://grsim_ros_bridge/resources/robot_marker_yellow.dae"
        self.yellow_robot_1_marker_pub.publish(marker_msg)

    #publish yellow robot marker
    def callback_yellow_robot_2_pose(self,msg):
        marker_msg = Marker()
        marker_msg.header = msg.header
        marker_msg.type = marker_msg.MESH_RESOURCE
        marker_msg.action = marker_msg.ADD
        marker_msg.pose = msg.pose
        marker_msg.scale.x = 1
        marker_msg.scale.y = 1
        marker_msg.scale.z = 1
        marker_msg.frame_locked = True
        marker_msg.mesh_use_embedded_materials = True
        marker_msg.mesh_resource = "package://grsim_ros_bridge/resources/robot_marker_yellow.dae"
        self.yellow_robot_2_marker_pub.publish(marker_msg)

    #publish yellow robot marker
    def callback_yellow_robot_3_pose(self,msg):
        marker_msg = Marker()
        marker_msg.header = msg.header
        marker_msg.type = marker_msg.MESH_RESOURCE
        marker_msg.action = marker_msg.ADD
        marker_msg.pose = msg.pose
        marker_msg.scale.x = 1
        marker_msg.scale.y = 1
        marker_msg.scale.z = 1
        marker_msg.frame_locked = True
        marker_msg.mesh_use_embedded_materials = True
        marker_msg.mesh_resource = "package://grsim_ros_bridge/resources/robot_marker_yellow.dae"
        self.yellow_robot_3_marker_pub.publish(marker_msg)

    #publish yellow robot marker
    def callback_yellow_robot_4_pose(self,msg):
        marker_msg = Marker()
        marker_msg.header = msg.header
        marker_msg.type = marker_msg.MESH_RESOURCE
        marker_msg.action = marker_msg.ADD
        marker_msg.pose = msg.pose
        marker_msg.scale.x = 1
        marker_msg.scale.y = 1
        marker_msg.scale.z = 1
        marker_msg.frame_locked = True
        marker_msg.mesh_use_embedded_materials = True
        marker_msg.mesh_resource = "package://grsim_ros_bridge/resources/robot_marker_yellow.dae"
        self.yellow_robot_4_marker_pub.publish(marker_msg)

    #publish yellow robot marker
    def callback_yellow_robot_5_pose(self,msg):
        marker_msg = Marker()
        marker_msg.header = msg.header
        marker_msg.type = marker_msg.MESH_RESOURCE
        marker_msg.action = marker_msg.ADD
        marker_msg.pose = msg.pose
        marker_msg.scale.x = 1
        marker_msg.scale.y = 1
        marker_msg.scale.z = 1
        marker_msg.frame_locked = True
        marker_msg.mesh_use_embedded_materials = True
        marker_msg.mesh_resource = "package://grsim_ros_bridge/resources/robot_marker_yellow.dae"
        self.yellow_robot_5_marker_pub.publish(marker_msg)

if __name__ == '__main__':
    rospy.init_node('marker_publisher_node', anonymous=False)
    marker_pub = marker_publisher()
    rospy.spin()
