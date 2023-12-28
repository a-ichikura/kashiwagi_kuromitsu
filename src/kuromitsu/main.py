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

if __name__ == "__main__":
    introduction.hello()
    print("hello done")
   # situation_2.scene_3()
    #print("scene3 done ")
    #situation_2.scene_4()
    #print("scene4 done ")
    
