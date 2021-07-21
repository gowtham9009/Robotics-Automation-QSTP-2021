#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def hello():
    rospy.init_node('hello', anonymous=True)
    pub = rospy.Publisher('hello', String, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        hello_str = 'Hello,' 
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__' :
    try:
        hello()
    except rospy.ROSInterruptException:
        pass
