#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import sys
from argparse import ArgumentParser

# Note : This code is based on python 2.7

def get_option():
    argparser = ArgumentParser()
    argparser.add_argument('-T', '--token', help='Token value from Slack api')
    argparser.add_argument('-C', '--channel', help='Channel id from Slack channel')
    return argparser.parse_args()

def main():
    print("This is script for sending.")
    args = get_option()
    
    token = args.token
    channel = args.channel
    
    if token is None or channel is None:
        print('please set args')
        sys.exit(1)

    url = "https://slack.com/api/chat.postMessage"
    
    headers = {"Authorization": "Bearer "+ token}
    data  = {
    'channel': channel,
    'text': 'This is a test.'
    }
    r = requests.post(url, headers=headers, data=data)
    print("return ", r.json())

if __name__ == '__main__':
    main()