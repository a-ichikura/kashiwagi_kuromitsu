#!/usr/bin/python3.6                                                                                                                                                                                       
# -*- coding: utf-8 -*-                                                                                                                                                                                    

import rospy
import time
from std_msgs.msg import String
from std_msgs.msg import UInt16
from std_msgs.msg import ColorRGBA
import module
from robotmodel import *
from playsound import playsound

scene_node = module.Scene_node()
# rospy.init_node("situation_node")                                                                                                                                                                        

def eye(mode):
    time.sleep(2)
    scene_node.eye(mode)

def cheek_led(r,g,b,brightness=10,mode=1,blink=3,duration=1,rainbow_hue=1):
    scene_node.cheek_led(r,g,b,brightness,mode,blink,duration,rainbow_hue)

def ume_led(r,g,b,brightness=10,mode=1,blink=3,duration=1,rainbow_hue=1):
    scene_node.ume_led(r,g,b,brightness,mode,blink,duration,rainbow_hue)

##############################################################################

def scene_noon():
    ume_led(r=0,g=0,b=0,brightness=0)
    time.sleep(3)
    eye(5)
    playsound("/home/leus/Downloads/kashiwagi_voices/kashiwagi_troubled.mp3")

    time.sleep(3)
    act("uemuku")
    playsound("/home/leus/Downloads/kashiwagi_voices/kashiwagi_shokuinshitsu.mp3")
    
    eye(9)
    ume_led(r=255,g=192, b=203, brightness=15, mode=2, blink=20, duration=0)
    cheek_led(r=255,g=192,b=203,brightness=15,mode=2,blink=20,duration=0)
    playsound("/home/leus/Downloads/kashiwagi_voices/kashiwagi_joy.mp3")
    act("uemuki_patapata")

def scene_2():
    ume_led(r=0,g=0,b=255)
    cheek_led(r=0,g=0,b=255)
    eye(7)
    cheek_led(r=255,g=192,b=203)
    ume_led(r=255,g=255,b=0)
    
    
    eye(5)
    act("unazuku")
    
    eye(6)
    cheek_led(r=255,g=192,b=203)
    ume_led(r=255,g=192,b=203)
    act("speedy_patapata")

def scene_2_2():
    eye(9)
    ume_led(r=255,g=255,b=0,mode=3)
    cheek_led(r=255,g=255,b=0,mode=3)
    act("speedy_patapata")
    
def scene_3():
    eye(1)
    cheek_led(r=255,g=192,b=203)
    ume_led(r=255,g=255,b=0)
    act("right_patapata")
    
def colab():
    time.sleep(2)
    eye(9)
    cheek_led(r=255,g=105,b=180,brightness=10)
    ume_led(r=255,g=255,b=0,brightness=15)
    time.sleep(2)
    act("mofumofu")
    
