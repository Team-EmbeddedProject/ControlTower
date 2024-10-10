import os
import torch
from ultralytics import YOLO 
import cv2
import numpy as np
import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.qos import QoSProfile
from cv_bridge import CvBridge
from std_msgs.msg import Float32, Int16  # 수정된 부분: Int16을 std_msgs에서 불러옴
from sensor_msgs.msg import Image
from geometry_msgs.msg import Point
from interface_package.srv import TrashInfo

HOME_DIR = '/home/pi/workspace/ControlTower/src/ct_package'
MODEL_PATH = HOME_DIR + '/resource/best.pt'
SAVE_PATH = HOME_DIR + '/resource/stream_image.jpg'
STREAM_URL = 'http://127.0.0.1:8080/?action=stream'

class YOLODetector:
    def __init__(self, model_path, save_path):
        self.model = YOLO(model_path)
        self.save_path = save_path

    def process_frame(self, frame):
        results = self.model.predict(source=frame)
        annotated_frame = results[0].plot()
        cv2.imwrite(self.save_path, annotated_frame)

        midpoints = self.calculate_midpoints(results)
        labels_and_confidences = []
        for result in results:
            for box in result.boxes:
                label = self.model.names[int(box.cls)]
                confidence = box.conf.item()  # 신뢰도 값을 float로 변환
                labels_and_confidences.append((label, confidence))

        return labels_and_confidences, midpoints

    @staticmethod
    def calculate_midpoints(results):
        midpoints = []
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                mid_x = (x1 + x2) / 2
                mid_y = (y1 + y2) / 2
                mid_x = mid_x.item()
                mid_y = mid_y.item()
                midpoints.append((mid_x, mid_y))
        return midpoints

class TrashDetector(Node):
    def __init__(self):
        super().__init__('trash_detector')
        qos_profile = QoSProfile(depth=10)
        self.mode = 100  # 초기는 자동 모드
        self.mode_subscriber = self.create_subscription(Int16, 'mode', self.robot_mode_callback, 10)

        self.target_z = 0.0  # mm
        self.sonar_flag = False

        # Camera subscriber - 처음에는 구독하지 않음
        self.camera_subscription = None
        self.bridge = CvBridge()

        # Sonar Subscriber
        self.sonar_subscriber = self.create_subscription(
            Float32,
            'sonar_distance',
            self.sonar_listener_callback,
            qos_profile
        )

        # YOLO detector
        self.detector = YOLODetector(MODEL_PATH, SAVE_PATH)
        self.is_trash = False

        # Service client
        self.trash_info_client = self.create_client(TrashInfo, 'trash_detection')

        # Topic Publisher
        self.trash_point_publisher = self.create_publisher(Point, 'trash_point', qos_profile)
    
    def robot_mode_callback(self, msg):
        self.get_logger().info(f'Received mode: {msg.data}')
        self.mode = msg.data

    def start_camera_subscription(self):
        """카메라 토픽 구독 시작"""
        qos_profile = QoSProfile(depth=1)
        self.camera_subscription = self.create_subscription(
            Image,
            'camera_image',
            self.camera_listener_callback,
            qos_profile
        )
        self.get_logger().info('Camera subscription started')

    def stop_camera_subscription(self):
        """카메라 토픽 구독 중지"""
        if self.camera_subscription is not None:
            self.destroy_subscription(self.camera_subscription)
            self.camera_subscription = None
            self.get_logger().info('Camera subscription stopped')

    def camera_listener_callback(self, msg):
        self.get_logger().info('Subscribe Camera image')
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
            # 프레임 한 장 처리 후 구독 중지
            self.stop_camera_subscription()
            labels_and_confidences, midpoints = self.detector.process_frame(cv_image)

            for label, confidence in labels_and_confidences:
                if confidence >= 0.3: 
                    self.is_trash = True
                self.get_logger().info(f"Detected object: {label}, Confidence: {confidence:.2%}")

            if self.is_trash:
                for midpoint in midpoints:
                    point = Point()
                    point.x = midpoint[0]
                    point.y = midpoint[1]
                    point.z = self.target_z
                    self.trash_point_publisher.publish(point)
                    self.get_logger().info(f"Midpoint: {midpoint}")
            else:
                self.get_logger().info("Obstacle Avoidance")

        except Exception as e:
            self.get_logger().error(f'Error converting ROS Image message to OpenCV: {e}')

    def sonar_listener_callback(self, msg):
        # 초음파 센서 값이 30cm 이하일 때만 처리
        if self.mode == 100:  # 자동 모드
            if msg.data <= 30.0 and self.camera_subscription is None:
                # 로봇 주행 중지 로직 추가
                self.target_z = msg.data * 10  # mm 변환
                self.get_logger().info("Robot Moving Stop")
                self.get_logger().info(f"Sonar triggered. Distance: {self.target_z} mm")

                # 초음파 값이 트리거되면 카메라 구독 시작
                self.start_camera_subscription()

    def call_trash_service(self, label):
        if self.is_trash:
            request = TrashInfo.Request()
            request.robot_id = 1  # or other robot id
            request.timestamp = self.get_clock().now().to_msg()
            request.trash_type = label
            request.latitude = 128.613  # 적절한 위치로 수정 필요
            request.longitude = 35.8875

            self.future = self.trash_info_client.call_async(request)
            self.future.add_done_callback(self.service_response_callback)

    def service_response_callback(self, future):
        try:
            response = future.result()
            self.get_logger().info(f"Service response received: {response}")
        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")

def main(args=None):
    rclpy.init(args=args)
    trash_detector = TrashDetector()
    executor = MultiThreadedExecutor()
    executor.add_node(trash_detector)
    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            trash_detector.destroy_node()
            rclpy.shutdown()

if __name__ == '__main__':
    main()
