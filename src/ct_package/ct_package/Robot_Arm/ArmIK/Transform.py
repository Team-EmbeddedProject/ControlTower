#!/usr/bin/env python3
# encoding:utf-8
import cv2
import sys
import math
import numpy as np

# 현재 코드 파일의 경로
sys.path.append('/home/pi/ControlTower/src/ct_package/ct_package/Robot_Arm/Camera/')

# CalibrationConfig 모듈에서 필요한 설정을 불러오기
from CameraCalibration.CalibrationConfig import *

# 로봇 팔 원점(팬-틸트 중심)과 카메라 화면 중심 사이의 거리 (단위: cm)
image_center_distance = 20

# .npz 파일의 절대 경로 지정
map_param_path = '/home/pi/ControlTower/src/ct_package/ct_package/Robot_Arm/Camera/map_param'

# .npz 파일에서 매핑 파라미터 로드
param_data = np.load(map_param_path + '.npz')

# 각 픽셀의 실제 거리를 계산
map_param_ = param_data['map_param']

# 값 매핑 함수: 특정 범위의 숫자를 다른 범위로 변환
def leMap(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# 이미지의 픽셀 좌표를 로봇 팔의 좌표로 변환
# 예: (100, 100, (640, 320))의 좌표와 이미지 해상도를 입력
def convertCoordinate(x, y, size):
    x = leMap(x, 0, size[0], 0, 640)
    x = x - 320
    x_ = round(x * map_param_, 2)

    y = leMap(y, 0, size[1], 0, 480)
    y = 240 - y
    y_ = round(y * map_param_ + image_center_distance, 2)

    return x_, y_

# 실제 길이를 이미지의 픽셀 길이로 변환
# 예: (10, (640, 320))의 길이와 이미지 해상도를 입력
def world2pixel(l, size):
    l_ = round(l/map_param_, 2)
    l_ = leMap(l_, 0, 640, 0, size[0])
    return l_

# 검출된 객체의 ROI 영역 가져오기
# cv2.boxPoints(rect)의 네 개의 꼭짓점 값을 입력받아 극값 반환
def getROI(box):
    x_min = min(box[0, 0], box[1, 0], box[2, 0], box[3, 0])
    x_max = max(box[0, 0], box[1, 0], box[2, 0], box[3, 0])
    y_min = min(box[0, 1], box[1, 1], box[2, 1], box[3, 1])
    y_max = max(box[0, 1], box[1, 1], box[2, 1], box[3, 1])

    return (x_min, x_max, y_min, y_max)

# ROI 영역을 제외한 모든 부분을 검은색으로 변환
# 이미지, ROI 영역, 이미지 해상도를 입력받음
def getMaskROI(frame, roi, size):
    x_min, x_max, y_min, y_max = roi
    x_min -= 10
    x_max += 10
    y_min -= 10
    y_max += 10

    if x_min < 0:
        x_min = 0
    if x_max > size[0]:
        x_max = size[0]
    if y_min < 0:
        y_min = 0
    if y_max > size[1]:
        y_max = size[1]

    black_img = np.zeros([size[1], size[0]], dtype=np.uint8)
    black_img = cv2.cvtColor(black_img, cv2.COLOR_GRAY2RGB)
    black_img[y_min:y_max, x_min:x_max] = frame[y_min:y_max, x_min:x_max]
    
    return black_img

# 나무 블록의 중심 좌표 가져오기
# rect 객체, 블록 극값, 이미지 해상도, minAreaRect 함수에서 반환된 블록 길이 입력
def getCenter(rect, roi, size, square_length):
    x_min, x_max, y_min, y_max = roi
    # 블록 중심의 좌표에 따라 이미지 중심에 가까운 꼭짓점을 기준으로 정확한 중심 계산
    if rect[0][0] >= size[0]/2:
        x = x_max 
    else:
        x = x_min
    if rect[0][1] >= size[1]/2:
        y = y_max
    else:
        y = y_min

    # 블록 대각선 길이 계산
    square_l = square_length/math.cos(math.pi/4)

    # 길이를 이미지 픽셀 길이로 변환
    square_l = world2pixel(square_l, size)

    # 블록의 회전 각도에 따라 중심 계산
    dx = abs(math.cos(math.radians(45 - abs(rect[2]))))
    dy = abs(math.sin(math.radians(45 + abs(rect[2]))))
    if rect[0][0] >= size[0] / 2:
        x = round(x - (square_l/2) * dx, 2)
    else:
        x = round(x + (square_l/2) * dx, 2)
    if rect[0][1] >= size[1] / 2:
        y = round(y - (square_l/2) * dy, 2)
    else:
        y = round(y + (square_l/2) * dy, 2)

    return  x, y

# 회전 각도 계산
# 로봇 팔 끝의 좌표와 블록의 회전 각도 입력
def getAngle(x, y, angle):
    theta6 = round(math.degrees(math.atan2(abs(x), abs(y))), 1)
    angle = abs(angle)
    
    if x < 0:
        if y < 0:
            angle1 = -(90 + theta6 - angle)
        else:
            angle1 = theta6 - angle
    else:
        if y < 0:
            angle1 = theta6 + angle
        else:
            angle1 = 90 - theta6 - angle

    if angle1 > 0:
        angle2 = angle1 - 90
    else:
        angle2 = angle1 + 90

    if abs(angle1) < abs(angle2):
        servo_angle = int(500 + round(angle1 * 1000 / 240))
    else:
        servo_angle = int(500 + round(angle2 * 1000 / 240))
    return servo_angle
