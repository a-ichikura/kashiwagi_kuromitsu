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


def scene_2():
    ume_led(r=255,g=255,b=255,brightness=20)
    eye(1)
    act("slowly_patapata")


def scene_3():
    ume_led(r=255,g=255,b=255,brightness=10)
    eye(0)
    
def scene_4():
    eye(2)
    act("look_back")
    ume_led(r=0,g=0,b=255)
    cheek_led(r=0.g=0,b=255)

def scene_5():
    eye(0)
    cheek_led(r=255,g=192,b=203)
    ume_led(r=252,g=213,b=117)
    act("long_uemuku")

def scene_6():
    act("unazuku")

def scene_7():
    eye(6)
    cheek_led(r=255,g=192,b=203)
    ume_led(r=255,g=192,b=203)
    act("patapata")

def scene_8():
    eye(6)
    cheek_led(r=255,g=192,b=203)
    ume_led(r=252,g=213,b=117)
