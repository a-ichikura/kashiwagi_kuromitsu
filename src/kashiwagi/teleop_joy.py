#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import sensor_msgs.msg

from robotmodel import act

class TeleopJoy(object):

    def __init__(self):
        self.sub_joy = None
        self.prev_command = None
        self.subscribe()

    def __exit__(self):
        self.unsubscribe()

    def subscribe(self):
        self.sub_joy = rospy.Subscriber(
            '/joy',
            sensor_msgs.msg.Joy,
            callback=self.joy_callback,
            queue_size=1)

    def unsubscribe(self):
        if self.sub_joy is not None:
            self.sub_joy.unregister()

    def joy_callback(self, msg):
        rospy.loginfo('{}'.format(msg.buttons))
        buttons = "".join(map(str, msg.buttons))
        if self.prev_command == buttons:
            return
        self.prev_command = buttons
        if buttons == "0100000000000":
            print("maru")            
            act("speedy_patapata")
        elif buttons == "1000000000000":
            print("X")
        elif buttons == "0010000000000":
            print("sankaku")
            act("unazuku")
        elif buttons == "0001000000000":
            print("shikaku")
        elif buttons == "0000000000100":
            print("ps button")
            act("init_pose")            

if __name__ == '__main__':
    # rospy.init_node('teleop_joy')
    teleop = TeleopJoy()
    rospy.spin()
