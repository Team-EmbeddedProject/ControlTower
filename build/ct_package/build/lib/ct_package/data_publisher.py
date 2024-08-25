import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from interface_package.srv import TrashInfo
from builtin_interfaces.msg import Time

# 각종 데이터 퍼블리시 테스트 용임.
class DataPublisher(Node):
    def __init__(self):
        super().__init__('data_publisher')
        qos_profile = QoSProfile(depth=10)
        self.trash_info_client = self.create_client(TrashInfo, 'trash_detection')
        while not self.trash_info_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting...')

        self.call_trash_service("PLA")
        
        # self.timer = self.create_timer(10.0, self.timer_callback)
        
    def call_trash_service(self, label):
        request = TrashInfo.Request()
        request.robot_id = 1  # or other robot id
        request.timestamp = self.get_clock().now().to_msg()
        request.trash_type = label
        request.latitude = 0.0  # 적절한 위치로 수정 필요
        request.longitude = 0.0

        self.future = self.trash_info_client.call_async(request)
        self.future.add_done_callback(self.service_response_callback)

    def service_response_callback(self, future):
        try:
            response = future.result()
            self.sonar_flag = False
            self.is_trash = False
            self.get_logger().info(f"Service response received: {response}")
        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")

def main(args=None):
    rclpy.init(args=args)
    trash_publisher = DataPublisher()
    try:
        rclpy.spin(trash_publisher)
    except KeyboardInterrupt:
        pass
    finally:
        trash_publisher.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
