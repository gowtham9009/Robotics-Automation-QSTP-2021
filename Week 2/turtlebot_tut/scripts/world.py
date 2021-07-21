#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def world():
    rospy.init_node('world', anonymous=True)
    pub = rospy.Publisher('world', String, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        world_str = ' World!'
        pub.publish(world_str)
        rate.sleep()

if __name__ == '__main__' :
    try:
        world()
    except rospy.ROSInterruptException:
        pass

