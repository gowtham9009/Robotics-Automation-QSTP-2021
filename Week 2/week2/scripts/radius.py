#! /usr/bin/env python3

import rospy
from std_msgs.msg import *

def radius():
    pub = rospy.Publisher('radius', Float32, queue_size=1)
    rospy.init_node('radius', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        rad = 0.1
        rospy.loginfo(rad)
        pub.publish(rad)
        rate.sleep()

if __name__ == "__main__":
    try:
        radius()
    except rospy.ROSInterruptException:
        pass
