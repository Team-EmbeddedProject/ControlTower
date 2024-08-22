#!/usr/bin/env python3
# encoding:utf-8
import sys
sys.path.append('/home/pi/MasterPi/')
import time
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from ArmIK.InverseKinematics import *
from ArmIK.Transform import getAngle
from mpl_toolkits.mplot3d import Axes3D
from HiwonderSDK.Board import setBusServoPulse,getBusServoPulse, setPWMServoPulse, getPWMServoPulse
from InverseKinematics import IK
import logging

logger = logging.getLogger(__name__)
ik = IK('arm')
l1 = ik.l1
l4 = ik.l4
ik.setLinkLength(L1=l1+1.3, L4=l4)

class ArmIK:
    servo3Range = (500, 2500.0, 0, 180.0) #Pulse width, angle
    servo4Range = (500, 2500.0, 0, 180.0)
    servo5Range = (500, 2500.0, 0, 180.0)
    servo6Range = (500, 2500.0, 0, 180.0)

    def __init__(self):
        self.setServoRange()

    
    def setServoRange(self, servo3_Range=servo3Range, servo4_Range=servo4Range, servo5_Range=servo5Range, servo6_Range=servo6Range):
        #서보 모터가 움직일 수 있는 범위 설정
        self.servo3Range = servo3_Range
        self.servo4Range = servo4_Range
        self.servo5Range = servo5_Range
        self.servo6Range = servo6_Range
        #서보 모터의 스케일링 factor( theta 값을 이용해 실제 팔의 위치로 이동시키는데 필요한 값)
        self.servo3Param = (self.servo3Range[1] - self.servo3Range[0]) / (self.servo3Range[3] - self.servo3Range[2])
        self.servo4Param = (self.servo4Range[1] - self.servo4Range[0]) / (self.servo4Range[3] - self.servo4Range[2])
        self.servo5Param = (self.servo5Range[1] - self.servo5Range[0]) / (self.servo5Range[3] - self.servo5Range[2])
        self.servo6Param = (self.servo6Range[1] - self.servo6Range[0]) / (self.servo6Range[3] - self.servo6Range[2])

    def transformAngelAdaptArm(self, theta3, theta4, theta5, theta6):
        print(f'{theta3}, {theta4}, {theta5}, {theta6}')
        
        # (self.servo3Range[1] + self.servo3Range[0])/2 == 모터가 중간 위치에 오도록 하는 코드
        # servo3 = int(round(theta3 * self.servo3Param + (self.servo3Range[1] + self.servo3Range[0])/2)) 세타 값을 받아 서보모터의 실제위치로 이동
        servo3 = int(round(theta3 * self.servo3Param + (self.servo3Range[1] + self.servo3Range[0])/2))
        if servo3 > self.servo3Range[1] or servo3 < self.servo3Range[0]:
            logger.info('servo3(%s)out of range(%s, %s)', servo3, self.servo3Range[0], self.servo3Range[1])
            print('servo3(%s)out of range(%s, %s)', servo3, self.servo3Range[0], self.servo3Range[1])
            return False

        servo4 = int(round(theta4 * self.servo4Param + (self.servo4Range[1] + self.servo4Range[0])/2))
        if servo4 > self.servo4Range[1] or servo4 < self.servo4Range[0]:
            logger.info('servo4(%s)out of range(%s, %s)', servo4, self.servo4Range[0], self.servo4Range[1])
            print('servo4(%s)out of range(%s, %s)', servo4, self.servo4Range[0], self.servo4Range[1])
            return False

        servo5 = int(round((self.servo5Range[1] + self.servo5Range[0])/2 + (90.0 - theta5) * self.servo5Param)) 
        if servo5 > ((self.servo5Range[1] + self.servo5Range[0])/2 + 90*self.servo5Param) or servo5 < ((self.servo5Range[1] + self.servo5Range[0])/2 - 90*self.servo5Param):
            logger.info('servo5(%s)out of range(%s, %s)', servo5, self.servo5Range[0], self.servo5Range[1])
            print('servo5(%s)out of range(%s, %s)', servo5, self.servo5Range[0], self.servo5Range[1])
            return False

        if theta6 < -(self.servo6Range[3] - self.servo6Range[2])/2:
            servo6 = int(round(((self.servo6Range[3] - self.servo6Range[2])/2 + (90 + (180 + theta6))) * self.servo6Param))
        else:
            servo6 = int(round(((self.servo6Range[3] - self.servo6Range[2])/2 - (90 - theta6)) * self.servo6Param)) + self.servo6Range[0]
        if servo6 > self.servo6Range[1] or servo6 < self.servo6Range[0]:
            logger.info('servo6(%s)out of range(%s, %s)', servo6, self.servo6Range[0], self.servo6Range[1])
            print('servo6(%s)out of range(%s, %s)', servo6, self.servo6Range[0], self.servo6Range[1])
            return False
        return {"servo3": servo3, "servo4": servo4, "servo5": servo5, "servo6": servo6}

    def servosMove(self, servos, movetime=None):
        time.sleep(0.02)
        if movetime is None:
            max_d = 0
            for i in  range(0, 4):
                d = abs(getPWMServoPulse(i + 3) - servos[i]) # 목표 위치와 현재 서보 값의 차이를 계산
                if d > max_d:
                    max_d = d # 가장 많이 움직여야 하는 서보 모터를 판단
            movetime = int(max_d*1) # 최대 차이를 기준으로 움직인 시간 계산
        setPWMServoPulse(3, servos[0], movetime)
        setPWMServoPulse(4, servos[1], movetime)
        setPWMServoPulse(5, servos[2], movetime)
        setPWMServoPulse(6, servos[3], movetime)
        
#         setPWMServosPulse(movetime, 4, 3,servos[0], 4,servos[1], 5,servos[2], 6,servos[3])
        return movetime

    def setPitchRange(self, coordinate_data, alpha1, alpha2, da = 1):
        x, y, z = coordinate_data
        if alpha1 >= alpha2:
            da = -da # np.arange(alpha1, alpha2, da) 에서 alpha1 < alpha2이어야 하므로 -부호를 붙혀 작게 해준다..? 
        for alpha in np.arange(alpha1, alpha2, da):
            result = ik.getRotationAngle((x, y, z), alpha) #회전해야할 값을 받아옴
            if result:
                # 세타 값이 유효하면(범위 내에 존재한다면), 받아오기
                theta3, theta4, theta5, theta6 = result['theta3'], result['theta4'], result['theta5'], result['theta6']                
                servos = self.transformAngelAdaptArm(theta3, theta4, theta5, theta6) # 세타 값을 이용해 서보모터 움직이기
                print(servos)
                if servos != False:
                    return servos, alpha # 목표 위치 (x,y,z)에 도달하기 위한 servo와 alpha 값들 반환

        return False

    def setPitchRangeMoving(self, coordinate_data, alpha, alpha1, alpha2, movetime = None):
        
        x, y, z = coordinate_data
        result1 = self.setPitchRange((x, y, z), alpha, alpha1) # alpha ~ alpha1 에서 최적의 값 찾기
        result2 = self.setPitchRange((x, y, z), alpha, alpha2) # alpha ~ alpha2 에서 최적의 값 찾기
        
        # alpha ~ alpha1 방향으로 탐색
        if result1 != False:
            data = result1
        # alpha ~ alpha2 방향으로 탐색     
            if result2 != False:
                if abs(result2[1] - alpha) < abs(result1[1] - alpha):
                    data = result2
                    
        else:
            if result2 != False:
                data = result2
                
            else:   
                return False
        
        servos, alpha = data[0], data[1] 
        movetime = self.servosMove((servos["servo3"], servos["servo4"], servos["servo5"], servos["servo6"]), movetime)
        return servos, alpha, movetime # 서보 위치, 서보 위치의 각도, 이동 시간을 반환
 
if __name__ == "__main__":
    AK = ArmIK()
    # setPWMServoPulse(1, 2300, 1500)
    # print(AK.setPitchRangeMoving((0, 0, 0), -90, -90, 90))
    # print(AK.setPitchRangeMoving((0, 8, 10), -90, -90, 90))
    # setPWMServoPulse(1, 1500, 1500)
    # servos = AK.transformAngelAdaptArm(0, 0, 90, 90)
    # AK.servosMove((servos["servo3"], servos["servo4"], servos["servo5"], servos["servo6"]), 2000)
    # print(ik.getLinkLength())
    # print(AK.setPitchRangeMoving((0,6,14),0,-90, 90))
    # time.sleep(2)
    # print(AK.setPitchRangeMoving((-4.8, 15, 1.5), 0, -90, 0, 2000))
    # AK.drawMoveRange2D(-10, 10, 0.2, 10, 30, 0.2, 2.5, -90, 90, 1)
