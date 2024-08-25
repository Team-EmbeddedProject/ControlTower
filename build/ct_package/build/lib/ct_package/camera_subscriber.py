import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CameraSubscriber(Node):
    def __init__(self):
        super().__init__('camera_subscriber')
        self.subscription = self.create_subscription(
            Image,
            'camera_image',
            self.listener_callback,
            10
        )
        self.bridge = CvBridge()
        self.get_logger().info('Camera subscriber node has been started')

    def listener_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
            cv2.imshow('Camera Image', cv_image)
            cv2.waitKey(1)
        except Exception as e:
            self.get_logger().error(f'Error converting ROS Image message to OpenCV: {e}')

def main(args=None):
    rclpy.init(args=args)
    camera_subscriber = CameraSubscriber()
    try:
        rclpy.spin(camera_subscriber)
    except KeyboardInterrupt:
        pass
    finally:
        cv2.destroyAllWindows()
        camera_subscriber.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()