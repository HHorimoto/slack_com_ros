#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import rospy
import os
import math
from geometry_msgs.msg import Twist

# Note : This code is based on ROS Melodic and python 2.7

class SlackListener(object):
    def __init__(self, signal_text, token, channel, receive_url, cmd_vel='cmd_vel', angular_vel=math.radians(30), linear_vel=0.333, time_limit=3.0, limit=1):
        self.signal_text = signal_text
        self.token = token
        self.channel = channel
        self.receive_url = receive_url
        self.limit = limit # only latest msg.
        self.angular_vel = angular_vel
        self.linear_vel = linear_vel
        self.time_limit = time_limit
        self.publish = rospy.Publisher(cmd_vel, Twist, queue_size=10)
        self.start_flag = 0
        self.old_ts = None

    def spin(self):
        headers = {"Authorization": "Bearer "+self.token}
        params = {
        "channel": self.channel,
        "limit": self.limit
        }
        
        r = requests.get(self.receive_url, headers=headers, params=params)
        info = r.json()
        ts = info['messages'][0]['ts']
        raw_text = info['messages'][0]['text']
        
        # wait signal text
        if (raw_text == self.signal_text) and (self.start_flag == 0):
            rospy.loginfo("Get Signal")
            self.start_flag = 1
            
        tm = rospy.get_time()
        
        if self.start_flag:
            if self.old_ts != ts:
                # for time limit
                self.start_time = rospy.get_time()
                
                # do action for received text
                rospy.loginfo("Receive new text [%s]", raw_text)
                raw_text = raw_text.lower()
                self.twist = Twist()
                if raw_text == 'forward':
                    self.twist.linear.x = abs(self.linear_vel)
                elif raw_text == 'back':
                    self.twist.linear.x = -abs(self.linear_vel)
                elif raw_text == 'left':
                    self.twist.angular.z = abs(self.angular_vel)
                elif raw_text == 'right':
                    self.twist.angular.z = -abs(self.angular_vel)
                elif raw_text == self.signal_text:
                    rospy.loginfo("This is signal text [%s]", raw_text)
                else:
                    rospy.logwarn("Unknown text [%s]", raw_text)
                    
                self.old_ts = ts
            if tm - self.start_time > self.time_limit:
                self.twist = Twist()
                # rospy.loginfo("Expired")
            self.publish.publish(self.twist)
            

def main():
    script_name = os.path.basename(__file__)
    node_name = os.path.splitext(script_name)[0]
    rospy.init_node(node_name)
    
    # param
    wait_time = rospy.get_param("~wait_time")
    signal_text = rospy.get_param("~signal_text")
    token = rospy.get_param("~token")
    channel = rospy.get_param("~channel")
    receive_url = rospy.get_param("~receive_url")
    
    rospy.sleep(wait_time) # for waiting signal

    rate = rospy.Rate(10)
    slack_listener = SlackListener(signal_text, token, channel, receive_url)

    while not rospy.is_shutdown():
        slack_listener.spin()
        rate.sleep()

if __name__ == '__main__':
    main()