#!/usr/bin/env python3
# encoding:utf-8

import rclpy
from rclpy.node import Node

import cv2
import sys
import math
import numpy as np

from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Point

class CoordinateTransformerNode(Node):
    def __init__(self):
        super().__init__('coordinate_transformer_node')

        # The distance between the origin of the robotic arm (center of pan-tilt) and the center of the camera screen in cm.
        self.image_center_distance = 20

        # Declare parameters for map_param_path, image_width, and image_height
        self.declare_parameter('map_param_path', '/home/pi/MasterPi/map_param')
        self.declare_parameter('image_width', 640)
        self.declare_parameter('image_height', 480)

        # Load parameters
        map_param_path = self.get_parameter('map_param_path').get_parameter_value().string_value
        self.image_width = self.get_parameter('image_width').get_parameter_value().integer_value
        self.image_height = self.get_parameter('image_height').get_parameter_value().integer_value

        # Load map parameters
        param_data = np.load(map_param_path + '.npz')
        self.map_param_ = param_data['map_param']

        # Image size
        self.image_size = (self.image_width, self.image_height)

        # Subscribers and Publishers
        self.subscription = self.create_subscription(
            Float32MultiArray,
            'image_coordinates',
            self.listener_callback,
            10)
        self.publisher = self.create_publisher(Point, 'robot_coordinates', 10)

    def listener_callback(self, msg):
        # Assuming msg.data contains [x, y]
        if len(msg.data) < 2:
            self.get_logger().error('Received invalid image coordinates')
            return

        x = msg.data[0]
        y = msg.data[1]

        # Perform coordinate transformation
        x_robot, y_robot = self.convertCoordinate(x, y, self.image_size)

        # Publish the robot coordinates
        point = Point()
        point.x = x_robot
        point.y = y_robot
        point.z = 0.0  # Assuming z is 0
        self.publisher.publish(point)

    # Value mapping function
    def leMap(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    # Convert pixel coordinates to robotic arm coordinates
    def convertCoordinate(self, x, y, size):
        x = self.leMap(x, 0, size[0], 0, 640)
        x = x - 320
        x_ = round(x * self.map_param_, 2)

        y = self.leMap(y, 0, size[1], 0, 480)
        y = 240 - y
        y_ = round(y * self.map_param_ + self.image_center_distance, 2)

        return x_, y_

    # Convert real-world length to pixel length
    def world2pixel(self, l, size):
        l_ = round(l / self.map_param_, 2)
        l_ = self.leMap(l_, 0, 640, 0, size[0])
        return l_

    # Get the ROI area
    def getROI(self, box):
        x_min = min(box[0, 0], box[1, 0], box[2, 0], box[3, 0])
        x_max = max(box[0, 0], box[1, 0], box[2, 0], box[3, 0])
        y_min = min(box[0, 1], box[1, 1], box[2, 1], box[3, 1])
        y_max = max(box[0, 1], box[1, 1], box[2, 1], box[3, 1])
        return (x_min, x_max, y_min, y_max)

    # Mask everything except the ROI area
    def getMaskROI(self, frame, roi, size):
        x_min, x_max, y_min, y_max = roi
        x_min -= 10
        x_max += 10
        y_min -= 10
        y_max += 10

        x_min = max(x_min, 0)
        x_max = min(x_max, size[0])
        y_min = max(y_min, 0)
        y_max = min(y_max, size[1])

        black_img = np.zeros([size[1], size[0]], dtype=np.uint8)
        black_img = cv2.cvtColor(black_img, cv2.COLOR_GRAY2RGB)
        black_img[y_min:y_max, x_min:x_max] = frame[y_min:y_max, x_min:x_max]
        return black_img

    # Get the center coordinate of the wooden block
    def getCenter(self, rect, roi, size, square_length):
        x_min, x_max, y_min, y_max = roi

        # Select the vertex closest to the image center as the reference point
        x = x_max if rect[0][0] >= size[0]/2 else x_min
        y = y_max if rect[0][1] >= size[1]/2 else y_min

        # Calculate the diagonal length of the block
        square_l = square_length / math.cos(math.pi / 4)

        # Convert the length to pixel length
        square_l = self.world2pixel(square_l, size)

        # Calculate the center based on the rotation angle
        dx = abs(math.cos(math.radians(45 - abs(rect[2]))))
        dy = abs(math.sin(math.radians(45 + abs(rect[2]))))
        if rect[0][0] >= size[0] / 2:
            x = round(x - (square_l / 2) * dx, 2)
        else:
            x = round(x + (square_l / 2) * dx, 2)
        if rect[0][1] >= size[1] / 2:
            y = round(y - (square_l / 2) * dy, 2)
        else:
            y = round(y + (square_l / 2) * dy, 2)

        return x, y

    # Get the rotation angle
    def getAngle(self, x, y, angle):
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
    
def main(args=None):
    rclpy.init(args=args)
    node = CoordinateTransformerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
