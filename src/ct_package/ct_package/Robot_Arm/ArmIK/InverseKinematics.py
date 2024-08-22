#!/usr/bin/env python3
# encoding: utf-8
# 4DOF robotic arm inverse kinematics: according to the given coordinates (x,y,z) and the pitch angle to, caculate the rotation angle of each joint.
# 2020/07/20 Aiden
import logging
from math import *

# CRITICAL, ERROR, WARNING, INFO, DEBUG
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class IK:
    # Inverse Kinematics = 로봇의 끝부분을 특정 위치나 방향으로 이동시키고자 할 때, 각 관절이 어떻게 움직여야 하는지를 계산하는 방법
    # 로봇 팔의 링크 길이 링크는 로봇 구조에서 각각 어디를 의미하는 걸까?
    # pump 모드랑 arm 모드의 차이점? 각각 어디다 쓰는건데? 
    l1 = 8.00
    l2 = 6.50
    l3 = 6.20
    l4 = 0.00
    l5 = 4.70
    l6 = 4.46
    alpha = degrees(atan(l6 / l5)) 

    def __init__(self, arm_type): 
        self.arm_type = arm_type # 무언가를 집은 후 들어 올리는 상태
        if self.arm_type == 'pump':
            self.l4 = sqrt(pow(self.l5, 2) + pow(self.l6, 2))  
        elif self.arm_type == 'arm': # 일반적인 팔 상태
            self.l4 = 10.00  

    def setLinkLength(self, L1=l1, L2=l2, L3=l3, L4=l4, L5=l5, L6=l6):
        self.l1 = L1
        self.l2 = L2
        self.l3 = L3
        self.l4 = L4
        self.l5 = L5
        self.l6 = L6
        if self.arm_type == 'pump':
            self.l4 = sqrt(pow(self.l5, 2) + pow(self.l6, 2))
            self.alpha = degrees(atan(self.l6 / self.l5))

    def getLinkLength(self):
        if self.arm_type == 'pump':
            return {"L1":self.l1, "L2":self.l2, "L3":self.l3, "L4":self.l4, "L5":self.l5, "L6":self.l6}
        else:
            return {"L1":self.l1, "L2":self.l2, "L3":self.l3, "L4":self.l4}
        
    # 관절의 회전 각도를 계산하는 메서드
    def getRotationAngle(self, coordinate_data, Alpha):
        X, Y, Z = coordinate_data # 로봇 팔의 목표 좌표
        if self.arm_type == 'pump':
            Alpha -= self.alpha # 로봇 팔의 특정 각도
        
        theta6 = degrees(atan2(Y, X)) #  X-Y 평면에서 로봇 팔의 방향
 
        P_O = sqrt(X*X + Y*Y) # X와 Y 좌표의 거리
        CD = self.l4 * cos(radians(Alpha))
        PD = self.l4 * sin(radians(Alpha)) 
        # 로봇 팔의 연결 지점 간의 거리
        AF = P_O - CD           # 로봇 팔의 첫 번째 링크가 목표 위치에 도달하기 위해 남은 수평 거리
        CF = Z - self.l1 - PD   # 로봇 팔의 첫 번째 링크가 목표 위치에 도달하기 위해 남은 수직 거리
        AC = sqrt(pow(AF, 2) + pow(CF, 2)) # 첫 번째 링크가 목표 위치에 도달하기 위해 남은 거리
        if round(CF, 4) < -self.l1:
            logger.debug('Height below 0, CF(%s)<l1(%s)', CF, -self.l1)
            print(f'Height below 0, CF({CF})<l1({-self.l1})')
            return False
        if self.l2 + self.l3 < round(AC, 4): 
            logger.debug('Can not form linkage structure, l2(%s) + l3(%s) < AC(%s)', self.l2, self.l3, AC)
            print(f'Can not form linkage structure, l2({self.l2}) + l3({self.l3}) < AC({AC}), Alpha = {Alpha}')
            # print(f'P_O = {P_O} CD = {CD} PD = {PD} AF = {AF} CF = {CF} AC = {AC} Alpha = {Alpha}')
            return False

        cos_ABC = round((pow(self.l2, 2) + pow(self.l3, 2) - pow(AC, 2))/(2*self.l2*self.l3), 4) 
        if abs(cos_ABC) > 1:
            logger.debug('Can not form linkage structure, abs(cos_ABC(%s)) > 1', cos_ABC)
            print(f'Can not form linkage structure, abs(cos_ABC({cos_ABC})) > 1')
            return False
        ABC = acos(cos_ABC) 
        theta4 = 180.0 - degrees(ABC)

        # find theta5
        CAF = acos(AF / AC)
        cos_BAC = round((pow(AC, 2) + pow(self.l2, 2) - pow(self.l3, 2))/(2*self.l2*AC), 4) 
        if abs(cos_BAC) > 1:
            logger.debug('Can not form linkage structure, abs(cos_BAC(%s)) > 1', cos_BAC)
            print(f'Can not form linkage structure, abs(cos_BAC({cos_BAC})) > 1')
            return False
        if CF < 0:
            zf_flag = -1
        else:
            zf_flag = 1
        theta5 = degrees(CAF * zf_flag + acos(cos_BAC))

        # find theta3
        theta3 = Alpha - theta5 + theta4
        if self.arm_type == 'pump':
            theta3 += self.alpha

        return {"theta3":theta3, "theta4":theta4, "theta5":theta5, "theta6":theta6} 
            
if __name__ == '__main__':
    ik = IK('arm')
    # ik.setLinkLength(L1=ik.l1 + 1.30, L4=ik.l4)
    print('linkage length：', ik.getLinkLength())
    # print(ik.getRotationAngle((0, ik.l4, ik.l1 + ik.l2 + ik.l3), 0))
