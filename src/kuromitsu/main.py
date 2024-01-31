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
import introduction
import colab
import academic_day

if __name__ == "__main__":
    key = "null"
    while not key == "exit":
        key = input("input key:")
        if key == "intro":
            academic_day.intro()
        elif key == "1":
            academic_day.situation_1()
        elif key == "2" :
            academic_day.situation_2()
        elif key == "3" :
            academic_day.situation_3()
        elif key == "colab" :
            academic_day.colab()
    
    
    
    
