#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import rospy
import time
from std_msgs.msg import String
from std_msgs.msg import UInt16
from std_msgs.msg import ColorRGBA

import situation_1
import situation_2
import situation_3
import colab
import academic_day

if __name__ == "__main__":
    #academic_day.scene_noon()
    #academic_day.scene_3()
    # academic_day.colab()
    key = "null"
    while not key == "exit":
        key = input("input key:")
        if key == "noon":
            academic_day.scene_noon()
        elif key == "evening":
            academic_day.scene_3()
        elif key == "colab" :
            academic_day.colab()
