import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from interface_package.msg import TrashInfo
from builtin_interfaces.msg import Time

# 각종 데이터 퍼블리시 테스트 용임.
class DataPublisher(Node):
    def __init__(self):
        super().__init__('data_publisher')
        qos_profile = QoSProfile(depth=10)
        self.ID = 1
        self.location = [0.0 ,0.0, 0.0]
        self.classification = "PLA"
        
        # Create a subscriber to the 'trash_info' topic
        self.trash_subscriber = self.create_subscription(
            TrashInfo,
            'trash_info',
            self.listener_callback,
            qos_profile
        )
        
        # Create a publisher for the String message
        self.trash_publisher = self.create_publisher(
            TrashInfo,
            'trash_info',
            qos_profile
        )
        
        self.timer = self.create_timer(1.0, self.timer_callback)
        
    def timer_callback(self):
        msg = TrashInfo()
        msg.robot_id = self.ID
        msg.timestamp = self.get_clock().now().to_msg()
        msg.trash_type = self.classification
        msg.trash_location = self.location
        
        self.trash_publisher.publish(msg)
        self.get_logger().info(f'Publishing data: {msg.trash_type}')
    
    def listener_callback(self, msg):
        # Publish the formatted message
        self.get_logger().info('Subscribe data - ID:{0} date:{1} location:{2} classification:{3}'.format(
            msg.robot_id,        # robot id 
            msg.timestamp,       # robot date 
            msg.trash_location,  # robot location
            msg.trash_type       # robot classification 
            ))

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
