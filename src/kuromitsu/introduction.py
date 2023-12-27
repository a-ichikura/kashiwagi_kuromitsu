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

def eye(mode):
    scene_node.eye(mode)

def cheek_led(r,g,b,brightness=10,mode=1,blink=3,duration=1,rainbow_hue=1):
    scene_node.cheek_led(r,g,b,brightness,mode,blink,duration,rainbow_hue)

def ume_led(r,g,b,brightness=10,mode=1,blink=3,duration=1,rainbow_hue=1):
    scene_node.ume_led(r,g,b,brightness,mode,blink,duration,rainbow_hue)

#############################################
#######　編集するのはこの下から！ ###########
#############################################

def scene_1():
    time.sleep(2)
    eye(4)
    cheek_led(r=255,g=0,b=0,mode=3)
    act("tap")

def scene_2():
    time.sleep(2)
    eye(6)
    cheek_led(r=255,g=20,b=147,brightness=20,mode=1)
    act("high-touch")
    
def scene_3():
    time.sleep(2)
    eye(0)
    cheek_led(r=255,g=105,b=180,brightness=10)
    act("carry")
    
def scene_4():
    time.sleep(2)
    eye(0)
    cheek_led(r=255,g=105,b=180,brightness=10)
    act("wave")

def scene_5():
    time.sleep(2)
    eye(6)
    cheek_led(r=255,g=105,b=180,brightness=20)
    act("catch")

def scene_6():
    time.sleep(2)
    eye(4)
    cheek_led(r=255,g=69,b=0,brightness=20)
    act("against")
    
def scene_7():
    time.sleep(2)
    eye(2)
    cheek_led(r=255,g=20,b=147,brightness=20)
    act("pass_hand")

def scene_normal():
    time.sleep(2)
    eye(0)
    cheek_led(r=255,g=105,b=180,brightness=10)
    act("normal")
