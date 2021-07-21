#! /usr/bin/env python3

from __future__ import print_function

import rospy
from std_msgs.msg import *
from turtlebot_tut.srv import angvel, angvelResponse
from geometry_msgs import *



def compute_ang_vel_1(req):
    resp1 = angvelResponse(0.1/req.rad)
    print(resp1)
    return resp1
    
def compute_ang_vel_server():
    rospy.init_node('compute_ang_vel_server')
    server = rospy.Service('compute_ang_vel', angvel, compute_ang_vel_1)
    print("ready to calc angular velocity")
    rospy.spin()

if __name__ == "__main__":
    compute_ang_vel_server()