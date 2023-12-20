#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import rospy
import time
from std_msgs.msg import String
from std_msgs.msg import UInt16
from std_msgs.msg import ColorRGBA
from module import *

def scene_1():
    #cheek_led(r=10,g=255,b=0,mode=1)
    #print("{} done".format("cheek_led"))
    act("test") #動作の名前を入力
    
