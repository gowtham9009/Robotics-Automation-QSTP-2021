This is a directory containing the package of week 2 tasks which include learning the concepts of publisher and subscriber , service and clients.
And publishing commands to cmd_vel to move the turtlebot accordingly .
For the first task of publisher and subscriber:
    The files hello.py and world.py publish to the file helloworld.py which acts as a subscriber node to both the topic /hello and /world.

For the second task of service and client:
    trajectory_service.py acts as the service node while trajectory_client acts as the client node that recieves information of the coordinates and plots them on a graph.
    
For the third task of combining all the above tasks has the following:
  The first subtask:
    radius.py publishes the radius with the topic name /hello.
    
  The second subtask:
    compute_ang_vel_server.py subscribes the value of radius and calculates the angular velocity 
    with a preset value of linear velocity and publishes it.
    
  The third subtask:
    infinite.py subscribes to both radius.py and compute_ang_vel_server.py and publishes the modified
    values of the linear and angualr velocities to cmd_vel to make the turtlebot in gazebo move in a shape
    of eight(or infinite symbol).
    
 The responses of the above publishing files has been recorded in the bagfiles folder.
  
