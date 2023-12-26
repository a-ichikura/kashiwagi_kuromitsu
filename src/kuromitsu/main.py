#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import rospy
import time
from std_msgs.msg import String
from std_msgs.msg import UInt16
from std_msgs.msg import ColorRGBA

import situation_1

if __name__ == "__main__":
    situation_1.scene_5()
    print("scene_5 done")
    situation_1.scene_6()
    print("scene_6 done")
