# ## trash_info
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
 
    def call_trash_service(self, label):
        request = TrashInfo.Request()
        request.timestamp = self.get_clock().now().to_msg()
        request.robot_id = 1  # or other robot id
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

## robot_log
# import rclpy
# from rclpy.node import Node
# from interface_package.msg import RobotLog
# from builtin_interfaces.msg import Time

# class RobotLogPublisher(Node):
#     def __init__(self):
#         super().__init__('robot_log_publisher')
#         self.publisher_ = self.create_publisher(RobotLog, 'robot_log', 10)
#         # 0.5초마다 publish_log_message 함수를 호출하는 타이머
#         self.timer = self.create_timer(0.5, self.publish_log_message)

#     def publish_log_message(self):
#         msg = RobotLog()
#         msg.timestamp = self.get_clock().now().to_msg()
#         msg.robot_id = 1
#         msg.row_id = 1  # 테스트용 row ID
#         msg.col_id = 1  # 테스트용 col ID

#         self.publisher_.publish(msg)
#         self.get_logger().info(f'Published RobotLog: robot_id={msg.robot_id}, row_id={msg.row_id}, col_id={msg.col_id}')

# def main(args=None):
#     rclpy.init(args=args)
#     robot_log_publisher = RobotLogPublisher()

#     try:
#         rclpy.spin(robot_log_publisher)  # spin을 사용하여 타이머가 실행되도록 함
#     except KeyboardInterrupt:
#         pass
#     finally:
#         robot_log_publisher.destroy_node()
#         rclpy.shutdown()

# if __name__ == '__main__':
#     main()
