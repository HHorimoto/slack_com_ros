cmake_minimum_required(VERSION 3.0.2)
project(slack_com_ros)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)
catkin_package()