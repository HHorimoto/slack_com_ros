# slack_com_ros

**This package provides communication between Slack and ROS**

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
