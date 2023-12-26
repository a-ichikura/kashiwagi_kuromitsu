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

def test_1():
    time.sleep(2)
    eye(4) #目を真剣にする
    cheek_led(255,105,180,10)
    act("fetch_ball") #ballを取りに行く
    print("go to fetch ball")
    time.sleep(2)

def test_2():
    act("grab_ball") #ballを持つ
    time.sleep(2)
    eye(6) #喜ぶ
    cheek_led(255,20,147,10)
    print("say やった〜")
    #やったーと言う

def test_3():
    act("grab_ball")
    time.sleep(4)
    act("tos_ball") #ballを投げる
    print("say ナイスボール")

def test_4():
    time.sleep(2)
    print("move start")
    cheek_led(r=255,g=105,b=180,brightness=10,mode=1)
    act("nod") #test
    eye(2)
    print("done")

def scene_1():
    time.sleep(2)
    eye(0)
    cheek_led(r=255,g=105,b=180,brightness=10)

def scene_2():
    eye(0)
    cheek_led(r=255,g=105,b=180,brightness=10)
    act("patapata")
    act("normal")

def scene_3():
    eye(4)
    cheek_led(r=255,g=105,b=180,brightness=10)
    act("look_left")
    
def scene_4():
    eye(4)
    cheek_led(r=255,g=105,b=180,brightness=10)
    act("look_left")

def scene_5():
    time.sleep(2)
    eye(3)
    cheek_led(r=255,g=105,b=180,brightness=3)
    act("sleepy")
    
