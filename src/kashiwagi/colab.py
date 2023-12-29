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

def test():
    print("start test")
    act("test")
    print("done")

def scene_1():
    time.sleep(2)
    eye(0)
    cheek_led(r=255,g=105,b=180,brightness=10)
    ume_led(r=255,g=0,b=0,brightness=10,mode=2)

def scene_2():
    time.sleep(2)
    eye(6)
    cheek_led(r=255,g=105,b=180,brightness=20)
    ume_led(r=255,g=255,b=0,brightness=15)

def scene_3():
    time.sleep(2)
    eye(2)
    cheek_led(r=0,g=0,b=0,brightness=0)
    ume_led(r=135,g=206,b=235,brightness=10)

def scene_4():
    time.sleep(2)
    eye(5)
    cheek_led(r=0,g=0,b=255,brightness=10)
    ume_led(r=0,g=0,b=255,brightness=20,mode=2)

def scene_5():
    time.sleep(2)
    eye(9)
    cheek_led(r=255,g=105,b=180,brightness=10)
    ume_led(r=255,g=255,b=0,brightness=15)

def scene_6():
    time.sleep(2)
    act("mofumofu")
    
