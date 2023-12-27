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
        buttons = msg.buttons
        if self.prev_command == buttons:
            return
        self.prev_command = buttons
        if buttons[1] == 1:
            print("maru")            
            act("speedy_patapata")
        elif buttons[0] == 1:
            print("X")
        elif buttons[2] == 1:
            print("sankaku")
            act("unazuku")
        elif buttons == [3]:
            print("shikaku")
        elif buttons[10] == 1:
            print("ps button")
            act("init_pose")
            

if __name__ == '__main__':
    # rospy.init_node('teleop_joy')
    teleop = TeleopJoy()
    rospy.spin()
