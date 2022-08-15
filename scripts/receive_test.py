#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import sys
from argparse import ArgumentParser

# Note : This code is based on python 2.7

def get_option():
    argparser = ArgumentParser()
    argparser.add_argument('-T', '--token', help='Token value from Slack api')
    argparser.add_argument('-C', '--channel', help='Conversation ID from Slack api')
    return argparser.parse_args()

def main():
    print("This is script for receiving.")
    args = get_option()
    
    token = args.token
    channel = args.channel
    
    if token is None or channel is None:
        print('please set args')
        sys.exit(1)

    url = "https://slack.com/api/conversations.history"
    headers = {"Authorization": "Bearer "+token}
    params = {
    "channel": channel,
    "limit": 1 # only latest msg.
    }
    r = requests.get(url, headers=headers, params=params)
    print("return ", r.json())

if __name__ == '__main__':
    main()