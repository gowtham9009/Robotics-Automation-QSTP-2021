#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

hello =""
world = ""

def callback1(data):
    global hello
    hello = data.data

def callback2(data):
    global world
    world = data.data

def helloworld():
    rospy.init_node('helloworld')
    sub1 = rospy.Subscriber('hello', String, callback1)
    sub2 = rospy.Subscriber('world', String, callback2)
    pub = rospy.Publisher('helloworld', String, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        tot = hello + world
        print(tot)
        pub.publish(tot)
        rate.sleep()

if __name__ == '__main__' :
    try:
        helloworld()
    except rospy.ROSInterruptException:
        pass
