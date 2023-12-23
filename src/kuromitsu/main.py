#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import rospy
import time
from std_msgs.msg import String
from std_msgs.msg import UInt16
from std_msgs.msg import ColorRGBA

import situation_1

if __name__ == "__main__":
    situation_1.test_1()
    print("done test1")
    situation_1.test_2()
    print("done test2")
    situation_1.test_3()
    print("done test3")
    #situation_1.scene_2()
