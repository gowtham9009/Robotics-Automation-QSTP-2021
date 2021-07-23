#! /usr/bin/env python3

from __future__ import print_function

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import *
from turtlebot_tut.srv import angvel

rospy.init_node('turtle_vel')
rospy.wait_for_service('compute_ang_vel')
ang_vel = rospy.ServiceProxy('compute_ang_vel', angvel)
velocity = Twist()

def callback(msg):
    velocity.linear.x = 0.1
    velocity.linear.y = 0.0
    velocity.linear.z = 0.0
    velocity.angular.x = 0.0
    velocity.angular.y = 0.0
    angular_velocity = ang_vel(msg.data)
    velocity.angular.z = angular_velocity.ang_vel

pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
sub = rospy.Subscriber('radius', Float32, callback)

rate = rospy.Rate(10)

while not rospy.is_shutdown():
    pub.publish(velocity)
    rate.sleep()