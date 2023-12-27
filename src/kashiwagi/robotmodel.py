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


class ArmROSRobotInterface(ROSRobotInterfaceBase):

    def __init__(self, *args, **kwargs):
        namespace = kwargs.get('namespace', None)
        namespace = '/{}'.format(namespace) if namespace else ''
        self.joint_names = rospy.get_param(
            namespace
            + '/kxr_fullbody_controller/joints')
        super(ArmROSRobotInterface, self).__init__(*args, **kwargs)
        self.servo_on_off_client = actionlib.SimpleActionClient(
            namespace + '/kxr_fullbody_controller/servo_on_off',
            ServoOnOffAction)
        self.servo_on_off_client.wait_for_server()

    def servo_on(self, joint_names=None):
        if joint_names is None:
            joint_names = self.joint_names
        goal = ServoOnOffGoal()
        client = self.servo_on_off_client
        if client.get_state() == actionlib_msgs.msg.GoalStatus.ACTIVE:
            client.cancel_goal()
            client.wait_for_result(timeout=rospy.Duration(10))
        self.angle_vector(self.angle_vector(), 0.1)
        self.wait_interpolation()
        rospy.sleep(1.0)
        goal.joint_names = joint_names
        goal.servo_on_states = [True] * len(joint_names)
        client.send_goal(goal)

    def servo_off(self, joint_names=None):
        if joint_names is None:
            joint_names = self.joint_names
        goal = ServoOnOffGoal()
        client = self.servo_on_off_client
        if client.get_state() == actionlib_msgs.msg.GoalStatus.ACTIVE:
            client.cancel_goal()
            client.wait_for_result(timeout=rospy.Duration(10))
        goal.joint_names = joint_names
        goal.servo_on_states = [False] * len(joint_names)
        client.send_goal(goal)

    @property
    def fullbody_controller(self):
        return dict(
            controller_type='kxr_fullbody_controller',
            controller_action='kxr_fullbody_controller/follow_joint_trajectory',
            controller_state='kxr_fullbody_controller/state',
            action_type=control_msgs.msg.FollowJointTrajectoryAction,
            joint_names=self.joint_names,
        )

    def default_controller(self):
        return [self.fullbody_controller]

# rospy.init_node('interface_controller')
r = RobotModel()
urdf_path = resolve_filepath("", "package://kxr_models/urdf/kashiwagi.urdf")
with open(urdf_path) as f:
    r.load_urdf_file(f)

for j in r.joint_list:
    if j.max_joint_velocity == 0.0:
        j.max_joint_velocity = 10.0
ri = ArmROSRobotInterface(r, controller_timeout=1000)

def servo_on():
    ri.servo_on()

def servo_off():
    ri.servo_off()

def act(act_name):
    ri.servo_on()
    json_filepath = "/home/leus/kashiwagi_movie.json"
    if os.path.exists(json_filepath):
        try:
            with open(json_filepath) as f:
                motion_dict = json.load(f)
        except json.JSONDecodeError as e:
            print(e)

        if len(motion_dict) > 0:
            angles = motion_dict[act_name]
            print(angles)
            if len(angles) > 0:
                ri.angle_vector(angles[0],3)
                ri.wait_interpolation()
            for av in angles[1:]:
                ri.angle_vector(av, 0.5)
                # ri.wait_interpolation()
    else:
        print("There is not such file.")    
    
    
