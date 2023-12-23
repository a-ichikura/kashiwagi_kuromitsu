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

def scene_1():
    time.sleep(2)
    eye(6)
    cheek_led(r=255,g=105,b=180,mode=1)
    time.sleep(3)
    eye(5)
    cheek_led(r=135,g=206,b=235,brightness=10,mode=1)
    time.sleep(3)
    eye(2)
    cheek_led(r=255,g=255,b=255,brightness=30,mode=3)
    #print("{} done".format("cheek_led"))
    #act("init") #動作の名前を入力
    
def scene_2():
    print("test start")
    act("quite")
    time.sleep(5)
    act("init")
