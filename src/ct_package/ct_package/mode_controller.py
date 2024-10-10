import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
from interface_package.srv import ModeNum

class ModeController(Node):
    def __init__(self):
        super().__init__('mode_controller')
        # 100: 자동, 200: 수동
        self.mode_server = self.create_service(ModeNum, 'change_mode', self.mode_change_callback)
        self.mode_publisher = self.create_publisher(Int16, 'mode', 10)

        self.get_logger().info("Mode Controller is running.")

    def mode_change_callback(self, request, response):
        mode_message = Int16()
        mode_message.data = request.mode

        self.mode_publisher.publish(mode_message)

        response.success = True
        self.get_logger().info(f'Published Mode Data - {mode_message.data}')
        return response

def main(args=None):
    rclpy.init(args=args)
    mode_controller = ModeController()

    try:
        rclpy.spin(mode_controller)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            mode_controller.destroy_node()
            rclpy.shutdown()

if __name__ == '__main__':
    main()
