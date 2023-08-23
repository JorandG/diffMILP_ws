#!/usr/bin/env python

import rospy
from gazebo_msgs.msg import ModelStates
from geometry_msgs.msg import PoseStamped

def model_states_callback(msg):
    try:
        robot_index = msg.name.index('diff_wheeled_robot')  # Replace with the actual robot name
        robot_pose = PoseStamped()
        robot_pose.pose = msg.pose[robot_index]
        pose_publisher.publish(robot_pose)
    except ValueError:
        pass

if __name__ == '__main__':
    rospy.init_node('robot_pose_publisher', anonymous=True)
    
    pose_publisher = rospy.Publisher('/custom_robot/pose', PoseStamped, queue_size=10)
    
    rospy.Subscriber('/gazebo/model_states', ModelStates, model_states_callback)
    
    rospy.spin()

