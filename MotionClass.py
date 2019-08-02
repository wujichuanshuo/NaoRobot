# _*_coding:utf-8_*_
import argparse
import cv2
import numpy as np
import numpy as shap
import numpy as ndarray
from numpy import ndarray
import time
import math
import time
import sys
import PIL
from PIL import Image, ImageDraw
from naoqi import ALProxy, ALModule, ALBroker
#1.Ready 准备
#2.HoldingPole 握竿
#3.AddressingTheBall 击球准备
#4.Batting 击球
#5.ReceivingPole 收杆
#6.MoveEnd 运动结束

class MotionClass(object):
    def __init__(self, IP, PORT):
        self.IP = IP
        self.PORT = PORT

    def TouchFirstHead(self):
        MemoryProxy = ALProxy("ALMemory", self.IP, self.PORT)
        while True:
            flag1 = MemoryProxy.getData("FrontTactilTouched")
            flag2 = MemoryProxy.getData("MiddleTactilTouched")
            flag3 = MemoryProxy.getData("RearTactilTouched")
            if flag1 == 1.0:
                self.HoldingPole()
                break
            if flag2 == 1.0:
                self.AddressingTheBall()
                self.Batting(0.3)
                self.ReceivingPole()
                break
            if flag3 == 1.0:

                Move=self.Move(self.IP,self.PORT)
                Move.MoveT(1,-1)
                self.MoveEnd()
                break

    def Stand(self):
        MotionProxy = ALProxy("ALRobotPosture", self.IP, self.PORT)
        MotionProxy.goToPosture("StandInit", 0.5)

    class Move():
        def __init__(self, robotIP, PORT):
            self.robotIP = robotIP
            self.PORT = PORT


        def MoveT(self, x, y, their=0):
            motionProxy = ALProxy("ALMotion", self.robotIP, self.PORT)
            motionProxy.setStiffnesses("Body", 1.0)
            time.sleep(1.0)
            motionProxy.setMoveArmsEnabled(True, True)
            their=math.atan(x/y)
            print their
            motionProxy.moveTo(0,0, their, [["MaxStepX", 0.04], ["MaxStepY", 0.14], ["MaxStepTheta", 0.3],["MaxStepFrequency", 0.6], ["StepHeight", 0.02], ["TorsoWx", 0.0],["TorsoWy", 0.0]])
            motionProxy.moveTo(math.sqrt(x*x+y*y),0, 0, [["MaxStepX", 0.04], ["MaxStepY", 0.14], ["MaxStepTheta", 0.3],["MaxStepFrequency", 0.6], ["StepHeight", 0.02], ["TorsoWx", 0.0],["TorsoWy", 0.0]])

        def HuDu(self, x):
            return -x * math.pi / 180.0

        def MoveToBall(self, x, y):
            z = math.atan(x / y)
            z = self.HuDu(z)
            self.MoveT(0, 0, z)
            x = math.sqrt(x ** 2.0 + y ** 2.0)
            self.MoveT(x, 0, 0)

    def Ready(self):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([0.4])
        keys.append([[-0.161001, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("HeadYaw")
        times.append([0.4])
        keys.append([[0.00640312, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("LAnklePitch")
        times.append([0.4])
        keys.append([[0.0874194, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("LAnkleRoll")
        times.append([0.4])
        keys.append([[-0.109114, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("LElbowRoll")
        times.append([0.4])
        keys.append([[-0.972515, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("LElbowYaw")
        times.append([0.4])
        keys.append([[-1.61381, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("LHand")
        times.append([0.4])
        keys.append([[1, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("LHipPitch")
        times.append([0.4])
        keys.append([[0.126315, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("LHipRoll")
        times.append([0.4])
        keys.append([[0.117297, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("LHipYawPitch")
        times.append([0.4])
        keys.append([[-0.17046, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("LKneePitch")
        times.append([0.4])
        keys.append([[-0.0894577, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("LShoulderPitch")
        times.append([0.4])
        keys.append([[1.06762, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("LShoulderRoll")
        times.append([0.4])
        keys.append([[-0.0583338, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("LWristYaw")
        times.append([0.4])
        keys.append([[-0.06447, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("RAnklePitch")
        times.append([0.4])
        keys.append([[0.0874194, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("RAnkleRoll")
        times.append([0.4])
        keys.append([[0.109102, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("RElbowRoll")
        times.append([0.4])
        keys.append([[1.0539, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("RElbowYaw")
        times.append([0.4])
        keys.append([[1.56924, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("RHand")
        times.append([0.4])
        keys.append([[0.999333, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("RHipPitch")
        times.append([0.4])
        keys.append([[0.126321, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("RHipRoll")
        times.append([0.4])
        keys.append([[-0.11736, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("RHipYawPitch")
        times.append([0.4])
        keys.append([[-0.17046, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("RKneePitch")
        times.append([0.4])
        keys.append([[-0.0894577, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("RShoulderPitch")
        times.append([0.4])
        keys.append([[1.07998, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("RShoulderRoll")
        times.append([0.4])
        keys.append([[0.145688, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("RWristYaw")
        times.append([0.4])
        keys.append([[-0.230143, [3, -0.146667, 0], [3, 0, 0]]])

        try:
            motion = ALProxy("ALMotion", self.IP, self.PORT)
            motion.angleInterpolationBezier(names, times, keys)
        except BaseException, err:
            print err

    def HoldingPole(self):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([0.44])
        keys.append([[-0.161001, [3, -0.16, 0], [3, 0, 0]]])

        names.append("HeadYaw")
        times.append([0.44])
        keys.append([[0.00640312, [3, -0.16, 0], [3, 0, 0]]])

        names.append("LAnklePitch")
        times.append([0.44])
        keys.append([[0.0874194, [3, -0.16, 0], [3, 0, 0]]])

        names.append("LAnkleRoll")
        times.append([0.44])
        keys.append([[-0.109114, [3, -0.16, 0], [3, 0, 0]]])

        names.append("LElbowRoll")
        times.append([0.44, 0.8, 1.2, 2, 2.64, 3.28])
        keys.append([[-0.972515, [3, -0.16, 0], [3, 0.12, 0]], [-1.05058, [3, -0.12, 0], [3, 0.133333, 0]],
                     [-1.0489, [3, -0.133333, -0.00167726], [3, 0.266667, 0.00335452]],
                     [-0.918823, [3, -0.266667, 0], [3, 0.213333, 0]],
                     [-0.92859, [3, -0.213333, 0.00976688], [3, 0.213333, -0.00976688]],
                     [-1.49481, [3, -0.213333, 0], [3, 0, 0]]])

        names.append("LElbowYaw")
        times.append([0.44, 0.8, 1.2, 2, 2.64, 3.28])
        keys.append([[-1.61381, [3, -0.16, 0], [3, 0.12, 0]], [-1.69328, [3, -0.12, 0], [3, 0.133333, 0]],
                     [-1.68096, [3, -0.133333, -0.0123203], [3, 0.266667, 0.0246406]],
                     [-1.54325, [3, -0.266667, 0], [3, 0.213333, 0]],
                     [-1.54415, [3, -0.213333, 0.000898817], [3, 0.213333, -0.000898817]],
                     [-1.56182, [3, -0.213333, 0], [3, 0, 0]]])

        names.append("LHand")
        times.append([0.44, 0.8, 1.2, 2, 2.64, 3.28])
        keys.append(
            [[1, [3, -0.16, 0], [3, 0.12, 0]], [1.73002e-05, [3, -0.12, 1.27351e-07], [3, 0.133333, -1.41501e-07]],
             [1.71587e-05, [3, -0.133333, 1.41501e-07], [3, 0.266667, -2.83002e-07]],
             [0, [3, -0.266667, 0], [3, 0.213333, 0]], [0, [3, -0.213333, 0], [3, 0.213333, 0]],
             [0, [3, -0.213333, 0], [3, 0, 0]]])

        names.append("LHipPitch")
        times.append([0.44])
        keys.append([[0.126315, [3, -0.16, 0], [3, 0, 0]]])

        names.append("LHipRoll")
        times.append([0.44])
        keys.append([[0.117297, [3, -0.16, 0], [3, 0, 0]]])

        names.append("LHipYawPitch")
        times.append([0.44])
        keys.append([[-0.17046, [3, -0.16, 0], [3, 0, 0]]])

        names.append("LKneePitch")
        times.append([0.44])
        keys.append([[-0.0894577, [3, -0.16, 0], [3, 0, 0]]])

        names.append("LShoulderPitch")
        times.append([0.44, 0.8, 1.2, 2, 2.64, 3.28])
        keys.append([[1.06762, [3, -0.16, 0], [3, 0.12, 0]], [1.06936, [3, -0.12, 0], [3, 0.133333, 0]],
                     [1.06883, [3, -0.133333, 0], [3, 0.266667, 0]], [1.15966, [3, -0.266667, 0], [3, 0.213333, 0]],
                     [1.14672, [3, -0.213333, 0], [3, 0.213333, 0]], [1.85061, [3, -0.213333, 0], [3, 0, 0]]])

        names.append("LShoulderRoll")
        times.append([0.44, 0.8, 1.2, 2, 2.64, 3.28])
        keys.append(
            [[-0.0583338, [3, -0.16, 0], [3, 0.12, 0]], [0.0396207, [3, -0.12, -0.00735619], [3, 0.133333, 0.00817355]],
             [0.0477943, [3, -0.133333, 0], [3, 0.266667, 0]], [-0.0583338, [3, -0.266667, 0], [3, 0.213333, 0]],
             [-0.0193417, [3, -0.213333, -0.0138528], [3, 0.213333, 0.0138528]],
             [0.0247832, [3, -0.213333, 0], [3, 0, 0]]])

        names.append("LWristYaw")
        times.append([0.44, 0.8, 1.2, 2, 2.64, 3.28])
        keys.append(
            [[-0.06447, [3, -0.16, 0], [3, 0.12, 0]], [-0.111321, [3, -0.12, 0.0113426], [3, 0.133333, -0.0126028]],
             [-0.136306, [3, -0.133333, 0.0249854], [3, 0.266667, -0.0499709]],
             [-1.53251, [3, -0.266667, 0.000251003], [3, 0.213333, -0.000200802]],
             [-1.53271, [3, -0.213333, 0.000200802], [3, 0.213333, -0.000200802]],
             [-1.55372, [3, -0.213333, 0], [3, 0, 0]]])

        names.append("RAnklePitch")
        times.append([0.44])
        keys.append([[0.0874194, [3, -0.16, 0], [3, 0, 0]]])

        names.append("RAnkleRoll")
        times.append([0.44])
        keys.append([[0.109102, [3, -0.16, 0], [3, 0, 0]]])

        names.append("RElbowRoll")
        times.append([0.44, 0.8, 1.2, 2, 2.64, 3.28])
        keys.append(
            [[1.0539, [3, -0.16, 0], [3, 0.12, 0]], [1.05841, [3, -0.12, -0.00451173], [3, 0.133333, 0.00501303]],
             [1.21781, [3, -0.133333, 0], [3, 0.266667, 0]], [1.00788, [3, -0.266667, 0], [3, 0.213333, 0]],
             [1.01705, [3, -0.213333, -0.00917346], [3, 0.213333, 0.00917346]],
             [1.51115, [3, -0.213333, 0], [3, 0, 0]]])

        names.append("RElbowYaw")
        times.append([0.44, 0.8, 1.2, 2, 2.64, 3.28])
        keys.append(
            [[1.56924, [3, -0.16, 0], [3, 0.12, 0]], [1.57235, [3, -0.12, -0.0022129], [3, 0.133333, 0.00245878]],
             [1.58325, [3, -0.133333, 0], [3, 0.266667, 0]], [1.57998, [3, -0.266667, 0], [3, 0.213333, 0]],
             [1.58325, [3, -0.213333, 0], [3, 0.213333, 0]], [1.53063, [3, -0.213333, 0], [3, 0, 0]]])

        names.append("RHand")
        times.append([0.44, 0.8, 1.2, 2, 2.64, 3.28])
        keys.append([[0.999333, [3, -0.16, 0], [3, 0.12, 0]], [0.999333, [3, -0.12, 0], [3, 0.133333, 0]],
                     [0.999333, [3, -0.133333, 0], [3, 0.266667, 0]], [0.999333, [3, -0.266667, 0], [3, 0.213333, 0]],
                     [0.00384884, [3, -0.213333, 0], [3, 0.213333, 0]], [0.253579, [3, -0.213333, 0], [3, 0, 0]]])

        names.append("RHipPitch")
        times.append([0.44])
        keys.append([[0.126321, [3, -0.16, 0], [3, 0, 0]]])

        names.append("RHipRoll")
        times.append([0.44])
        keys.append([[-0.11736, [3, -0.16, 0], [3, 0, 0]]])

        names.append("RHipYawPitch")
        times.append([0.44])
        keys.append([[-0.17046, [3, -0.16, 0], [3, 0, 0]]])

        names.append("RKneePitch")
        times.append([0.44])
        keys.append([[-0.0894577, [3, -0.16, 0], [3, 0, 0]]])

        names.append("RShoulderPitch")
        times.append([0.44, 0.8, 1.2, 2, 2.64, 3.28])
        keys.append([[1.07998, [3, -0.16, 0], [3, 0.12, 0]], [1.06651, [3, -0.12, 0], [3, 0.133333, 0]],
                     [1.37727, [3, -0.133333, 0], [3, 0.266667, 0]],
                     [1.12293, [3, -0.266667, 0.0104502], [3, 0.213333, -0.00836019]],
                     [1.11457, [3, -0.213333, 0], [3, 0.213333, 0]], [1.60266, [3, -0.213333, 0], [3, 0, 0]]])

        names.append("RShoulderRoll")
        times.append([0.44, 0.8, 1.2, 2, 2.64, 3.28])
        keys.append(
            [[0.145688, [3, -0.16, 0], [3, 0.12, 0]], [0.105972, [3, -0.12, 0.0185789], [3, 0.133333, -0.0206433]],
             [0.0280214, [3, -0.133333, 0], [3, 0.266667, 0]], [0.0858622, [3, -0.266667, 0], [3, 0.213333, 0]],
             [0.0492703, [3, -0.213333, 0], [3, 0.213333, 0]], [0.0892216, [3, -0.213333, 0], [3, 0, 0]]])

        names.append("RWristYaw")
        times.append([0.44, 0.8, 1.2, 2, 2.64, 3.28])
        keys.append(
            [[-0.230143, [3, -0.16, 0], [3, 0.12, 0]], [-0.237222, [3, -0.12, 0.00707905], [3, 0.133333, -0.00786561]],
             [-1.67342, [3, -0.133333, 0], [3, 0.266667, 0]], [-1.6675, [3, -0.266667, 0], [3, 0.213333, 0]],
             [-1.67342, [3, -0.213333, 0.00591661], [3, 0.213333, -0.00591661]],
             [-1.78388, [3, -0.213333, 0], [3, 0, 0]]])

        try:
            motion = ALProxy("ALMotion", self.IP, self.PORT)
            motion.angleInterpolationBezier(names, times, keys)
        except BaseException, err:
            print err

    def AddressingTheBall(self):
        names = list()
        times = list()
        keys = list()

        names.append("LElbowRoll")
        times.append([0.56, 1.28])
        keys.append([[-1.49913, [3, -0.2, 0], [3, 0.24, 0]], [-0.822284, [3, -0.24, 0], [3, 0, 0]]])

        names.append("LElbowYaw")
        times.append([0.56, 1.28])
        keys.append([[-1.56599, [3, -0.2, 0], [3, 0.24, 0]], [-1.67276, [3, -0.24, 0], [3, 0, 0]]])

        names.append("LHand")
        times.append([0.56, 1.28])
        keys.append([[0.0016481, [3, -0.2, 0], [3, 0.24, 0]], [0, [3, -0.24, 0], [3, 0, 0]]])

        names.append("LShoulderPitch")
        times.append([0.56, 1.28])
        keys.append([[1.84923, [3, -0.2, 0], [3, 0.24, 0]], [0.887498, [3, -0.24, 0], [3, 0, 0]]])

        names.append("LShoulderRoll")
        times.append([0.56, 1.28])
        keys.append([[0.0219138, [3, -0.2, 0], [3, 0.24, 0]], [-0.106043, [3, -0.24, 0], [3, 0, 0]]])

        names.append("LWristYaw")
        times.append([0.56, 1.28])
        keys.append([[-1.55368, [3, -0.2, 0], [3, 0.24, 0]], [-1.52446, [3, -0.24, 0], [3, 0, 0]]])

        names.append("RElbowRoll")
        times.append([0.56, 1.28])
        keys.append([[1.51428, [3, -0.2, 0], [3, 0.24, 0]], [0.855731, [3, -0.24, 0], [3, 0, 0]]])

        names.append("RElbowYaw")
        times.append([0.56, 1.28])
        keys.append([[1.5283, [3, -0.2, 0], [3, 0.24, 0]], [1.67814, [3, -0.24, 0], [3, 0, 0]]])

        names.append("RHand")
        times.append([0.56, 1.28])
        keys.append([[0.26088, [3, -0.2, 0], [3, 0.24, 0]], [0.991662, [3, -0.24, 0], [3, 0, 0]]])

        names.append("RShoulderPitch")
        times.append([0.56, 1.28])
        keys.append([[1.60092, [3, -0.2, 0], [3, 0.24, 0]], [0.83121, [3, -0.24, 0], [3, 0, 0]]])

        names.append("RShoulderRoll")
        times.append([0.56, 1.28])
        keys.append([[0.0886325, [3, -0.2, 0], [3, 0.24, 0]], [-0.054829, [3, -0.24, 0], [3, 0, 0]]])

        names.append("RWristYaw")
        times.append([0.56, 1.28])
        keys.append([[-1.79086, [3, -0.2, 0], [3, 0.24, 0]], [-1.80331, [3, -0.24, 0], [3, 0, 0]]])

        try:
            motion = ALProxy("ALMotion", self.IP, self.PORT)
            motion.angleInterpolationBezier(names, times, keys)
        except BaseException, err:
            print err

    def Batting(self, speed):
        names = list()
        times = list()
        keys = list()

        names.append("LElbowRoll")
        times.append([speed])
        keys.append([[-0.82493, [3, -0.12, 0], [3, 0, 0]]])

        names.append("LElbowYaw")
        times.append([speed])
        keys.append([[-1.6721, [3, -0.12, 0], [3, 0, 0]]])

        names.append("LHand")
        times.append([speed])
        keys.append([[1.72611e-05, [3, -0.12, 0], [3, 0, 0]]])

        names.append("LShoulderPitch")
        times.append([speed])
        keys.append([[0.890085, [3, -0.12, 0], [3, 0, 0]]])

        names.append("LShoulderRoll")
        times.append([speed])
        keys.append([[-0.0894722, [3, -0.12, 0], [3, 0, 0]]])

        names.append("LWristYaw")
        times.append([speed])
        keys.append([[0.0623137, [3, -0.12, 0], [3, 0, 0]]])

        names.append("RElbowRoll")
        times.append([speed])
        keys.append([[0.856824, [3, -0.12, 0], [3, 0, 0]]])

        names.append("RElbowYaw")
        times.append([speed])
        keys.append([[1.66928, [3, -0.12, 0], [3, 0, 0]]])

        names.append("RHand")
        times.append([speed])
        keys.append([[0.988543, [3, -0.12, 0], [3, 0, 0]]])

        names.append("RShoulderPitch")
        times.append([speed])
        keys.append([[0.835281, [3, -0.12, 0], [3, 0, 0]]])

        names.append("RShoulderRoll")
        times.append([speed])
        keys.append([[-0.0507674, [3, -0.12, 0], [3, 0, 0]]])

        names.append("RWristYaw")
        times.append([speed])
        keys.append([[-1.79725, [3, -0.12, 0], [3, 0, 0]]])

        try:
            motion = ALProxy("ALMotion", self.IP, self.PORT)
            motion.angleInterpolationBezier(names, times, keys)
        except BaseException, err:
            print err

    def ReceivingPole(self):
        names = list()
        times = list()
        keys = list()

        names.append("LElbowRoll")
        times.append([0.68, 1.64, 2.6])
        keys.append([[-0.822284, [3, -0.24, 0], [3, 0.32, 0]], [-0.822284, [3, -0.32, 0], [3, 0.32, 0]],
                     [-1.49604, [3, -0.32, 0], [3, 0, 0]]])

        names.append("LElbowYaw")
        times.append([0.68, 1.64, 2.6])
        keys.append([[-1.67276, [3, -0.24, 0], [3, 0.32, 0]], [-1.67276, [3, -0.32, 0], [3, 0.32, 0]],
                     [-1.5642, [3, -0.32, 0], [3, 0, 0]]])

        names.append("LHand")
        times.append([0.68, 1.64, 2.16, 2.6])
        keys.append([[0.00295589, [3, -0.24, 0], [3, 0.32, 0]], [0.00295589, [3, -0.32, 0], [3, 0.173333, 0]],
                     [0, [3, -0.173333, 0], [3, 0.146667, 0]], [0, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("LShoulderPitch")
        times.append([0.68, 1.64, 2.6])
        keys.append([[0.887498, [3, -0.24, 0], [3, 0.32, 0]], [0.887498, [3, -0.32, 0], [3, 0.32, 0]],
                     [1.84944, [3, -0.32, 0], [3, 0, 0]]])

        names.append("LShoulderRoll")
        times.append([0.68, 1.64, 2.6])
        keys.append(
            [[-0.106043, [3, -0.24, 0], [3, 0.32, 0]], [-0.0946152, [3, -0.32, -0.0114274], [3, 0.32, 0.0114274]],
             [0.0255408, [3, -0.32, 0], [3, 0, 0]]])

        names.append("LWristYaw")
        times.append([0.68, 1.64, 2.6])
        keys.append([[-1.55395, [3, -0.24, 0], [3, 0.32, 0]], [-1.55395, [3, -0.32, 0], [3, 0.32, 0]],
                     [-1.55396, [3, -0.32, 0], [3, 0, 0]]])

        names.append("RElbowRoll")
        times.append([0.68, 1.64, 2.6])
        keys.append([[0.855731, [3, -0.24, 0], [3, 0.32, 0]], [0.855731, [3, -0.32, 0], [3, 0.32, 0]],
                     [1.51303, [3, -0.32, 0], [3, 0, 0]]])

        names.append("RElbowYaw")
        times.append([0.68, 1.64, 2.6])
        keys.append([[1.67814, [3, -0.24, 0], [3, 0.32, 0]], [1.67814, [3, -0.32, 0], [3, 0.32, 0]],
                     [1.52665, [3, -0.32, 0], [3, 0, 0]]])

        names.append("RHand")
        times.append([0.68, 1.64, 2.6])
        keys.append([[0.991662, [3, -0.24, 0], [3, 0.32, 0]], [0.01, [3, -0.32, 0], [3, 0.32, 0]],
                     [0.250667, [3, -0.32, 0], [3, 0, 0]]])

        names.append("RShoulderPitch")
        times.append([0.68, 1.64, 2.6])
        keys.append([[0.83121, [3, -0.24, 0], [3, 0.32, 0]], [0.83121, [3, -0.32, 0], [3, 0.32, 0]],
                     [1.60089, [3, -0.32, 0], [3, 0, 0]]])

        names.append("RShoulderRoll")
        times.append([0.68, 1.64, 2.6])
        keys.append([[-0.054829, [3, -0.24, 0], [3, 0.32, 0]], [-0.054829, [3, -0.32, 0], [3, 0.32, 0]],
                     [0.0897188, [3, -0.32, 0], [3, 0, 0]]])

        names.append("RWristYaw")
        times.append([0.68, 1.64, 2.6])
        keys.append([[-1.80331, [3, -0.24, 0], [3, 0.32, 0]], [-1.80331, [3, -0.32, 0], [3, 0.32, 0]],
                     [-1.79052, [3, -0.32, 0], [3, 0, 0]]])

        try:
            motion = ALProxy("ALMotion", self.IP, self.PORT)
            motion.angleInterpolationBezier(names, times, keys)
        except BaseException, err:
            print err

    def MoveEnd(self):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([0.88])
        keys.append([[-0.16734, [3, -0.306667, 0], [3, 0, 0]]])

        names.append("HeadYaw")
        times.append([0.88])
        keys.append([[7.10543e-15, [3, -0.306667, 0], [3, 0, 0]]])

        names.append("LAnklePitch")
        times.append([0.88])
        keys.append([[0.0874194, [3, -0.306667, 0], [3, 0, 0]]])

        names.append("LAnkleRoll")
        times.append([0.88])
        keys.append([[-0.110027, [3, -0.306667, 0], [3, 0, 0]]])

        names.append("LElbowRoll")
        times.append([0.88])
        keys.append([[-1.49709, [3, -0.306667, 0], [3, 0, 0]]])

        names.append("LElbowYaw")
        times.append([0.88])
        keys.append([[-1.57219, [3, -0.306667, 0], [3, 0, 0]]])

        names.append("LHand")
        times.append([0.88])
        keys.append([[1.73002e-05, [3, -0.306667, 0], [3, 0, 0]]])

        names.append("LHipPitch")
        times.append([0.88])
        keys.append([[0.126915, [3, -0.306667, 0], [3, 0, 0]]])

        names.append("LHipRoll")
        times.append([0.88])
        keys.append([[0.118283, [3, -0.306667, 0], [3, 0, 0]]])

        names.append("LHipYawPitch")
        times.append([0.88])
        keys.append([[-0.170215, [3, -0.306667, 0], [3, 0, 0]]])

        names.append("LKneePitch")
        times.append([0.88])
        keys.append([[-0.0910193, [3, -0.306667, 0], [3, 0, 0]]])

        names.append("LShoulderPitch")
        times.append([0.88])
        keys.append([[1.84076, [3, -0.306667, 0], [3, 0, 0]]])

        names.append("LShoulderRoll")
        times.append([0.88])
        keys.append([[0.0769872, [3, -0.306667, 0], [3, 0, 0]]])

        names.append("LWristYaw")
        times.append([0.88])
        keys.append([[-1.55302, [3, -0.306667, 0], [3, 0, 0]]])

        names.append("RAnklePitch")
        times.append([0.88])
        keys.append([[0.0874194, [3, -0.306667, 0], [3, 0, 0]]])

        names.append("RAnkleRoll")
        times.append([0.88])
        keys.append([[0.11002, [3, -0.306667, 0], [3, 0, 0]]])

        names.append("RElbowRoll")
        times.append([0.88])
        keys.append([[1.51008, [3, -0.306667, 0], [3, 0, 0]]])

        names.append("RElbowYaw")
        times.append([0.88])
        keys.append([[1.54362, [3, -0.306667, 0], [3, 0, 0]]])

        names.append("RHand")
        times.append([0.88])
        keys.append([[0.245015, [3, -0.306667, 0], [3, 0, 0]]])

        names.append("RHipPitch")
        times.append([0.88])
        keys.append([[0.126918, [3, -0.306667, 0], [3, 0, 0]]])

        names.append("RHipRoll")
        times.append([0.88])
        keys.append([[-0.118308, [3, -0.306667, 0], [3, 0, 0]]])

        names.append("RHipYawPitch")
        times.append([0.88])
        keys.append([[-0.170215, [3, -0.306667, 0], [3, 0, 0]]])

        names.append("RKneePitch")
        times.append([0.88])
        keys.append([[-0.0910193, [3, -0.306667, 0], [3, 0, 0]]])

        names.append("RShoulderPitch")
        times.append([0.88])
        keys.append([[1.5798, [3, -0.306667, 0], [3, 0, 0]]])

        names.append("RShoulderRoll")
        times.append([0.88])
        keys.append([[0.0247619, [3, -0.306667, 0], [3, 0, 0]]])

        names.append("RWristYaw")
        times.append([0.88])
        keys.append([[-1.78209, [3, -0.306667, 0], [3, 0, 0]]])

        try:
            motion = ALProxy("ALMotion", self.IP, self.PORT)
            motion.angleInterpolationBezier(names, times, keys)
        except BaseException, err:
            print err

def main(RobotIP, PORT):
    Motion = MotionClass(RobotIP, PORT)
    Motion.Stand()
    Motion.Ready()
    while True:
        Motion.TouchFirstHead()



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.1.104",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)
