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
import introduction
import situation_1
import situation_2
import situation_3
import colab

import threading

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


def intro():
    time.sleep(2)
    eye(1)
    cheek_led(r=255,g=255,b=0,brightness=10)
    print("start")
    play_thread = threading.Thread(target=playsound, args=("/home/ichikura/toshima_ws/src/kashiwagi_kuromitsu/src/kuromitsu/voices/intro.wav", ))
    act_thread = threading.Thread(target=act, args=("hello", ))
    # playsound("/home/ichikura/toshima_ws/src/kashiwagi_kuromitsu/src/kuromitsu/voices/intro.wav")
    # act("hello")    
    act_thread.start()
    time.sleep(9.5)
    play_thread.start()
    act_thread.join()
    play_thread.join()
    servo_off()


def situation_1():
    time.sleep(2)
    eye(3)
    cheek_led(r=255,g=105,b=180,brightness=3)
    print("start")
    play_thread = threading.Thread(target=playsound, args=("/home/ichikura/toshima_ws/src/kashiwagi_kuromitsu/src/kuromitsu/voices/situation_1.wav", ))
    act_thread = threading.Thread(target=act, args=("sleepy_2", ))
    act_thread.start()
    time.sleep(9.5)
    play_thread.start()
    act_thread.join()
    play_thread.join()
    servo_off()


def situation_2():
    time.sleep(2)
    eye(10) #目はハートにする
    cheek_led(r=255,g=20,b=147,brightness=20)
    play_thread = threading.Thread(target=playsound, args=("/home/ichikura/toshima_ws/src/kashiwagi_kuromitsu/src/kuromitsu/voices/situation_2.wav", ))
    act_thread = threading.Thread(target=act, args=("pass_hand", ))
    act_thread.start()
    time.sleep(6.5)
    play_thread.start()
    act_thread.join()
    play_thread.join()
    servo_off()

def situation_3():
    time.sleep(2)
    eye(6)
    cheek_led(r=255,g=105,b=180,brightness=20)
    play_thread = threading.Thread(target=playsound, args=("/home/ichikura/toshima_ws/src/kashiwagi_kuromitsu/src/kuromitsu/voices/situation_3.wav", ))
    act_thread = threading.Thread(target=act, args=("catch", ))
    act_thread.start()
    time.sleep(5)
    play_thread.start()
    act_thread.join()
    play_thread.join()
    servo_off()

def colab():
    time.sleep(2)
    eye(0)
    cheek_led(r=255,g=105,b=180,brightness=10)
    play_thread = threading.Thread(target=playsound, args=("/home/ichikura/toshima_ws/src/kashiwagi_kuromitsu/src/kuromitsu/voices/colab.wav", ))
    act_thread = threading.Thread(target=act, args=("mofumofu",1, ))
    act_thread.start()
    time.sleep(6)
    play_thread.start()
    act_thread.join()
    play_thread.join()
    servo_off()



