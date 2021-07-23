#! /usr/bin/env python3

from __future__ import print_function

import sys
import rospy
from turtlebot_tut.srv import *
from std_msgs import *
from geometry_msgs import *
import matplotlib.pyplot as plt




def plot_points(x:float, y:float, theta:float, v:float, w: float):
    rospy.wait_for_service('trajectory')
    client = rospy.ServiceProxy('trajectory', trajectory)
    points = client(x, y, theta, v, w)
    return points.x1, points.y1

def trajectory_graph(x1:float, y1:float, v:float, w: float):

    plt.title(f"Unicycle Model: {v}, {w}")
    plt.xlabel("X-Coordinates")
    plt.ylabel("Y-Coordinates")
    plt.plot(x1, y1, color="red", alpha=0.75)
    #for i in range(len(x1)):
        #plt.scatter(x1[i], y1[i], color="red")

        # If you want to view the plot uncomment plt.show() and comment out plt.savefig()
    plt.show()
        # If you want to save the file, uncomment plt.savefig() and comment out plt.show()
    #plt.savefig(f"Unicycle_{v}_{w}.png")

if __name__ == "__main__":
    if len(sys.argv) == 6:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
        theta = float(sys.argv[3])
        v = float(sys.argv[4])
        w = float(sys.argv[5])
    
    else:
        print("%s [x y theta v w]"%sys.argv[0])
        sys.exit()
    
    print("The graph is:")
    print("%s"%x)
    print("%s"%y)
    print("%s"%theta)
    print("%s"%v)
    print("%s"%w)
    trajectory_graph(plot_points(x, y, theta, v, w)[0], plot_points(x, y, theta, v, w)[1], v, w)
 
 