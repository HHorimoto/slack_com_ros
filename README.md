# slack_com_ros

**This package provides communication between Slack and ROS**

<img src=./media/desc.png width=35% alt="description">

## Requirement
+ Ubuntu 18.04
+ ROS (Melodic)
+ Python 2.7.x

## Set Up
1. Download `centroidtracker_ros` package.

```shell
$ cd ~/catkin_ws/src/
$ git clone https://github.com/HHorimoto/centroidtracker_ros.git
$ cd ~/catkin_ws
$ catkin_make
```

2. Download necessary package for this package.

```shell
$ pip install requests # for requests
```

3. Set up `Create an App` for communication between Slack and ROS

This [link](./README_Slack_jp.md) is for japanese.

This link is for english. (I am sorry, it is still in preparation. so please look for setting up `Create an App` in internet.)

## Test Set Up

After you complete the setup, please verify that you can send and receive messages in `Slack` from python using following scripts `send_test` and `receive_test`.

### Send Test

```shell
$ roscd slack_com_ros/scripts/
$ ./send_test.py -T {Your Token number} -C {Your Channel ID}
```

see `Slack` if the script sends `This is a test.`.

### Receive Test

```shell
$ roscd slack_com_ros/scripts/
$ ./receive_test.py -T {Your Token number} -C {Your Channel ID}
```

see `Terminal` if the script prints latest `text`.

## How To Use

When you launch following launch script, you must set `Token Number` and `Channel ID`.
The robot moves accordingly, when a message is sent among `forward`, `back`, `left` and `right`, the robot moves accordingly.

```shell
$ roslaunch slack_com_ros slack_com_ros.launch token:={Your Token number} channel:={Your Channel ID}
```

### Parameters

+ ***signal_text*** : Text to signal the start.
    default : `START`

+ ***wait_time*** : Time for waitting signal.
    default : `1.0`

+ ***send_url*** : Slack api send url. I believe that you dont need to change it.
    default : `https://slack.com/api/chat.postMessage`

+ ***receive_url*** : Slack api receive url. I believe that you dont need to change it.
    default : `https://slack.com/api/conversations.history`

+ ***token*** : Token number that you got before.
    default : None

+ ***channel*** : Channel id that you got before.
    default : None