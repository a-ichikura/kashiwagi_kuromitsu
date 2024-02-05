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
import threading

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
    time.sleep(3)
    ume_led(r=0,g=0,b=0,brightness=0) #消す
    eye(5)
    sound_thread = threading.Thread(target=playsound,args=("/home/leus/Downloads/kashiwagi_voices/kashiwagi_troubled.mp3",))
    act_thread = threading.Thread(target=act, args=("uemuku",))

    act_thread.start()
    time.sleep(9.5)
    sound_thread.start()
    act_thread.join()
    sound_thread.join()

    time.sleep(3)
    playsound("/home/leus/Downloads/kashiwagi_voices/kashiwagi_shokuinshitsu.mp3")
    
    eye(9)
    ume_led(r=255,g=192, b=203, brightness=15, mode=2, blink=20, duration=0)
    cheek_led(r=255,g=192,b=203,brightness=15,mode=2,blink=20,duration=0)

    sound_thread = threading.Thread(target=playsound,args=("/home/leus/Downloads/kashiwagi_voices/kashiwagi_joy.mp3",))
    act_thread = threading.Thread(target=act,args=("uemuki_patapata",))

    act_thread.start()
    time.sleep(6)
    sound_thread.start()
    act_thread.join()
    sound_thread.join()
    time.sleep(3)
    servo_off()
    
def scene_2():
    #使わない
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
    #使わない
    eye(9)
    ume_led(r=255,g=255,b=0,mode=3)
    cheek_led(r=255,g=255,b=0,mode=3)
    act("speedy_patapata")
    
def scene_3():
    #またね
    #voice = matane
    time.sleep(3)
    eye(1)
    cheek_led(r=255,g=192,b=203)
    ume_led(r=255,g=255,b=0)
    sound_thread = threading.Thread(target=playsound,args=("/home/leus/Downloads/kashiwagi_voices/kashiwagi_matane.mp3",))
    act_thread = threading.Thread(target=act,args=("right_patapata",))

    act_thread.start()
    time.sleep(4)
    sound_thread.start()
    act_thread.join()
    sound_thread.join()
    servo_off()
    
def colab():
    time.sleep(2)
    eye(9)
    cheek_led(r=255,g=105,b=180,brightness=10)
    ume_led(r=255,g=255,b=0,brightness=15)
    time.sleep(2)

    sound_thread = threading.Thread(target=playsound,args=("/home/leus/Downloads/kashiwagi_voices/kashiwagi_yeah.mp3",))
    act_thread = threading.Thread(target=act,args=("mofumofu",))

    act_thread.start()
    time.sleep(3.5)
    sound_thread.start()
    act_thread.join()
    sound_thread.join()
    servo_off()

    
