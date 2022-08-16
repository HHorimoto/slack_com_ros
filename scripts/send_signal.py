#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import os
import requests

# Note : This code is based on ROS Melodic and python 2.7

def send_signal(text, token, channel, url):
    headers = {"Authorization": "Bearer "+ token}
    data  = {
    'channel': channel,
    'text': text
    }
    r = requests.post(url, headers=headers, data=data)
    info = r.json()
    raw_text = info['message']['blocks'][0]['elements'][0]['elements'][0]['text']
    rospy.loginfo("Send [%s] for signal", raw_text)    

def main():
    script_name = os.path.basename(__file__)
    node_name = os.path.splitext(script_name)[0]
    rospy.init_node(node_name)
    
    rospy.loginfo("Send Signal To Start")
    
    # param
    signal_text = rospy.get_param("~signal_text")
    token = rospy.get_param("~token")
    channel = rospy.get_param("~channel")
    send_url = rospy.get_param("~send_url")
    
    send_signal(signal_text, token, channel, send_url)

if __name__ == '__main__':
    main()