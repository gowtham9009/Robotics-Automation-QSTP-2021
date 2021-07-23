#! /usr/bin/env python3

from __future__ import print_function


import rospy
from turtlebot_tut.srv import trajectory,trajectoryResponse
from std_msgs import *
from geometry_msgs import *
import numpy as np

dt = 0.05
n = 50

    
class Unicycle:

    def step(self, req):
        self.req = req
        self.x= req.x
        self.y= req.y
        self.theta= req.theta
        self.v  = req.v
        self.w = req.w

            # Store the points of the trajectory to plot
        self.x_points = [self.x]
        self.y_points = [self.y]
        t= dt
        for i in range(0,(n-1)):
            self.theta = self.theta + i*self.w*t 
                
            self.x += self.v*np.cos(self.theta)*t
            self.y =  self.y + self.v*np.sin(self.theta)*t
                
            self.x_points.append(self.x)
            self.y_points.append(self.y)
                
        return trajectoryResponse(x1=(self.x_points), y1=(self.y_points))
        
                
if __name__== "__main__":
    rospy.init_node('trajectory')
    unicycle = Unicycle()
    ser = rospy.Service('trajectory', trajectory, unicycle.step)
    print('Ready to plot')
    rospy.spin()
        