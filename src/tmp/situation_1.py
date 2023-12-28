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
    eye(7)
    ume_led(r=255,g=0,b=0,brightness=20,mode=2,duration=0)
    cheek_led(r=0,g=0,b=255,brightness=0)

def scene_2():
    eye(7)
    ume_led(r=255,g=0, b=0, brightness=15, mode=2, blink=20, duration=0)
    
def scene_3():
    ume_led(r=0,g=0,b=0,brightness=0)
    eye(5)
    act("uemuku")
    time.sleep(5)
    

def scene_4():
    eye(9)
    ume_led(r=255,g=192, b=203, brightness=15, mode=2, blink=20, duration=0)
    cheek_led(r=255,g=192,b=203,brightness=15,mode=2,blink=20,duration=0)
    act("uemuki_patapata")


def scene_5():
    # umeが黄色
    # 目が楽しい
    # cheek ピンク
    eye(6)
    ume_led(r=255,g=255,b=0,brightness=20,mode=2)
    cheek_led(r=255,g=105,b=180,brightness=10)

def scene_6_1():
    time.sleep(2)
    eye(2)
    ume_led(r=0,g=0,b=255,brightness=20,mode=1)
    cheek_led(r=0,g=0,b=255,brightness=20,mode=1)
def scene_6_3():
    eye(8)
    ume_led(r=10, g=10, b=10, brightness=20,mode=3)
    cheek_led(r=10, b=10, g=10, brightness=20,mode=3)
    act("speedy_patapata")
def scene_8():
    act("speedy_patapata")






































def test_1():
    time.sleep(2)
    eye(5)
    time.sleep(3)
    ume_led(r=255,g=0,b=0,mode=2,brightness=20,blink=10,duration=0)
    act("patapata")

def test_2():
    time.sleep(2)
    eye(5)
    time.sleep(2)
    eye(7)
    # 鳴き声を送る
    ume_led(r=255,g=0,b=0,mode=2,brightness=30,blink=10,duration=1)
    time.sleep(5)
    # act("kubi_furifuri")
    act("unun")
    # act("test")
    time.sleep(5)
    
def test_3():
    eye(9)
    cheek_led(r=255,g=105,b=180,mode=1,brightness=10)
    ume_led(r=100,g=100,b=100,brightness=30,mode=3)
    act("patapata_and_kubi")

def test_4():
    time.sleep(2)
    print("start kubi furi")
    act("kubi_furifuri")
    time.sleep(5)

def test_5():
    time.sleep(2)
    eye(1)
    ume_led(r=255, g=105, b=180,brightness=20, mode=3)
    cheek_led(r=255, g=105, b=180,brightness=20, mode=1)
    act("test")
    time.sleep(2)
    eye(6)

def scene_100():
    time.sleep(2)
    eye(1)
    cheek_led(r=255,g=105,b=180,mode=1)
    time.sleep(5)

    eye(5)
    cheek_led(r=135,g=206,b=235,brightness=10,mode=1)
    ume_led(r=135,g=206,b=235,brightness=10,mode=1)
    time.sleep(5)
    eye(8)
    cheek_led(r=255,g=255,b=255,brightness=30,mode=3)
    ume_led(r=255,g=165,b=0,brightness=30,mode=1)
    #print("{} done".format("cheek_led"))

    #act("init") #動作の名前を入力


def test_1000():
    act("test")

def scene_200():
    act("test")


