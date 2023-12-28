#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import rospy
import time
from std_msgs.msg import String
from std_msgs.msg import UInt16
from std_msgs.msg import ColorRGBA
import module 
from robotmodel import *

scene_node = module.Scene_node()
# rospy.init_node("situation_node")

def eye(mode):
    time.sleep(2)
    scene_node.eye(mode)

def cheek_led(r,g,b,brightness=10,mode=1,blink=3,duration=1,rainbow_hue=1):
    scene_node.cheek_led(r,g,b,brightness,mode,blink,duration,rainbow_hue)

def ume_led(r,g,b,brightness=10,mode=1,blink=3,duration=1,rainbow_hue=1):
    scene_node.ume_led(r,g,b,brightness,mode,blink,duration,rainbow_hue)

#############################################
#######　編集するのはこの下から！ ###########
#############################################

def scene_1():
    eye(0)
    ume_led(r=229,g=163,b=35)
    act("arm_close")

def scene_2():
    eye(0)
    ume_led(r=229,g=163,b=35)
    act("right_patapata")

def scene_3():
    eye(3)
    ume_led(r=164,g=168,b=212)
    act("slowly_patapata")
    cheek_led(r=255,g=192,b=203)

def scene_4():
    eye(3)
    ume_led(r=164,g=168,b=212)
    cheek_led(r=255,g=192,b=203)

    
