import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge
import cv2
import numpy as np

class ShapeDetector(Node):
    def __init__(self):
        super().__init__('shape_detector')

        self.camera_active = True
        self.shape_detect_count = 0

        self.camera_subscription = self.create_subscription(
            Image,
            'camera_image',
            self.camera_listener_callback,
            10
        )
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        
        self.bridge = CvBridge()
        self.prev_twist = Twist() # 이전 속도
        self.timer = None

        self.get_logger().info("Shape detector node has been started.")

    def camera_listener_callback(self, msg):
        if not self.camera_active:
            return

        # ROS Image 메시지를 OpenCV 이미지로 변환
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        # 모양 감지
        result_image, shape = self.detect_shapes(cv_image)
        
        twist_msg = Twist()
        if shape is None:
            twist_msg = self.prev_twist
            self.get_logger().info("No shape detected: Maintaining previous velocity.")
        else:
            # 모양이 인식되면 일단 정지 후 처리
            twist_msg.linear.x = 0.0
            twist_msg.angular.z = 0.0
            self.cmd_vel_pub.publish(twist_msg)  # 즉시 정지
            self.shape_detect_count += 1
            self.get_logger().info(f"Shape detected {self.shape_detect_count} time(s).")

            # 모양에 따라 새로운 동작 설정
            if shape == "Rectangle":
                twist_msg.linear.x = 0.5  # 직진 신호
                twist_msg.angular.z = 0.0
                self.cmd_vel_pub.publish(twist_msg)
                self.get_logger().info("Rectangle detected: Moving forward.")
            elif shape == "L-Shape":
                self.timer = self.create_timer(2.0, self.turn_left_then_move_forward)

            self.camera_active = False
            self.create_timer(3.0, self.reactivate_camera)  # 3초 후 카메라 다시 활성화

        self.prev_twist = twist_msg

    def reactivate_camera(self):
        self.camera_active = True

    def turn_left_then_move_forward(self):
        twist_msg = Twist()
        twist_msg.linear.x = 0.0
        twist_msg.angular.z = 0.43  # 좌회전
        self.cmd_vel_pub.publish(twist_msg)
        self.get_logger().info("L-Shape detected: Turning left.")

        # 일정 시간이 지난 후 직진으로 변경
        self.timer.cancel()  # 타이머 취소
        self.timer = self.create_timer(2.0, self.move_forward_after_turn)

    def move_forward_after_turn(self):
        twist_msg = Twist()
        twist_msg.linear.x = 0.5  # 직진
        twist_msg.angular.z = 0.0
        self.cmd_vel_pub.publish(twist_msg)
        self.get_logger().info("Turning completed: Moving forward.")
        self.timer.cancel()  # 타이머 종료

    def detect_shapes(self, image):
        result_shape = None
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred, 50, 150)
        kernel = np.ones((5, 5), np.uint8)
        edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

        # 컨투어 찾기
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            area = cv2.contourArea(contour)
            if area < 500:
                continue

            epsilon = 0.02 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            # 네모 탐지
            if len(approx) == 4:
                x, y, w, h = cv2.boundingRect(approx)
                aspect_ratio = float(w) / h
                result_shape = "Rectangle"
                if 0.9 <= aspect_ratio <= 1.1:
                    cv2.putText(image, "Square", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                else:
                    cv2.putText(image, "Rectangle", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # L-Shape 탐지
            elif len(approx) >= 6:
                angles = []
                for i in range(len(approx)):
                    pt1 = approx[i][0]
                    pt2 = approx[(i + 1) % len(approx)][0]
                    pt3 = approx[(i + 2) % len(approx)][0]
                    v1 = pt2 - pt1
                    v2 = pt3 - pt2
                    angle = np.arctan2(v2[1], v2[0]) - np.arctan2(v1[1], v1[0])
                    angles.append(np.degrees(np.abs(angle)))

                count_90_deg = sum(80 <= angle <= 100 for angle in angles)
                if count_90_deg >= 2:
                    result_shape = "L-Shape"
                    x, y, w, h = cv2.boundingRect(approx)
                    cv2.putText(image, "L-Shape", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        return image, result_shape

    def stop_robot(self):
        stop_twist = Twist()
        stop_twist.linear.x = 0.0
        stop_twist.angular.z = 0.0
        self.cmd_vel_pub.publish(stop_twist)
        self.get_logger().info("Stopping robot before shutdown.")

def main(args=None):
    rclpy.init(args=args)
    shape_detector = ShapeDetector()

    try:
        rclpy.spin(shape_detector)
    except KeyboardInterrupt:
        shape_detector.get_logger().info('Node stopped cleanly')
    except Exception as e:
        shape_detector.get_logger().error(f'Error occurred: {e}')
    finally:
        if rclpy.ok():
            shape_detector.stop_robot()
            shape_detector.destroy_node()
            rclpy.shutdown()

if __name__ == '__main__':
    main()