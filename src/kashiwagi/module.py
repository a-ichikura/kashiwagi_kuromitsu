#x#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import rospy
import json
import os
import threading
from enum import Enum
from std_msgs.msg import String
from std_msgs.msg import UInt16
from std_msgs.msg import ColorRGBA 

import control_msgs.msg
from skrobot.interfaces.ros.base import ROSRobotInterfaceBase
from skrobot.model import RobotModel
from skrobot.viewers import TrimeshSceneViewer
from skrobot.utils.urdf import resolve_filepath
import numpy as np

import actionlib
import actionlib_msgs.msg
from kxr_controller.msg import ServoOnOffAction
from kxr_controller.msg import ServoOnOffGoal

class Scene_node:
    
    def __init__(self):
        self.eye_pub = rospy.Publisher("/eye_status", UInt16, queue_size=1)
        self.cheek_led_blink_pub = rospy.Publisher("/cheek/led_blink_time", UInt16, queue_size=1)
        self.cheek_led_duration = rospy.Publisher("/cheek/led_duration", UInt16, queue_size=1)
        self.cheek_led_mode = rospy.Publisher("/cheek/led_mode", UInt16, queue_size=1)
        self.cheek_led_rainbow_delta_hue = rospy.Publisher("/cheek/led_rainbow_delta_hue", UInt16, queue_size=1)
        self.cheek_led_rgb = rospy.Publisher("/cheek/led_rgb", ColorRGBA, queue_size=1)
        self.ume_led_blink_pub = rospy.Publisher("/ume/led_blink_time", UInt16, queue_size=1)
        self.ume_led_duration = rospy.Publisher("/ume/led_duration", UInt16, queue_size=1)
        self.ume_led_mode = rospy.Publisher("/ume/led_mode", UInt16, queue_size=1)
        self.ume_led_rainbow_delta_hue = rospy.Publisher("/ume/led_rainbow_delta_hue", UInt16, queue_size=1)
        self.ume_led_rgb = rospy.Publisher("/ume/led_rgb", ColorRGBA, queue_size=1)
        # rospy.init_node("modules")
        
    def eye(self,mode=0):
        mode_msg = UInt16()
        mode_msg.data = mode
        
        self.eye_pub.publish(mode_msg)

    def cheek_led(self,r,g,b,brightness=10,mode=1,blink=3,duration=1,rainbow_hue=1):
        
        color = ColorRGBA()
        color.r = r
        color.g = g
        color.b = b
        color.a = brightness
        
        blink_msg = UInt16()
        duration_msg = UInt16()
        mode_msg = UInt16()
        rainbow_hue_msg = UInt16()
        
        blink_msg.data = blink
        duration_msg.data = duration
        mode_msg.data = mode
        rainbow_hue_msg.data = rainbow_hue
        
        self.cheek_led_blink_pub.publish(blink_msg)
        self.cheek_led_duration.publish(duration_msg)
        self.cheek_led_mode.publish(mode_msg)
        self.cheek_led_rainbow_delta_hue.publish(rainbow_hue_msg)
        self.cheek_led_rgb.publish(color)

    def ume_led(self,r,g,b,brightness=10,mode=1,blink=3,duration=1,rainbow_hue=1):
            
        color = ColorRGBA()
        color.r = r
        color.g = g
        color.b = b
        color.a = brightness
        
        blink_msg = UInt16()
        duration_msg = UInt16()
        mode_msg = UInt16()
        rainbow_hue_msg = UInt16()
        
        blink_msg.data = blink
        duration_msg.data = duration
        mode_msg.data = mode
        rainbow_hue_msg.data = rainbow_hue
        
        self.ume_led_blink_pub.publish(blink_msg)
        self.ume_led_duration.publish(duration_msg)
        self.ume_led_mode.publish(mode_msg)
        self.ume_led_rainbow_delta_hue.publish(rainbow_hue_msg)
        self.ume_led_rgb.publish(color)    
    
