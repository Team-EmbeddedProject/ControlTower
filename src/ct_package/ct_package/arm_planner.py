import rclpy 
from rclpy.node import Node
from rclpy.qos import QoSProfile
from geometry_msgs.msg import Point

class ArmPlanner(Node):
    """
    ROS 2 노드: 실세계 3D 좌표를 로봇 팔의 목표 좌표로 변환하여 발행합니다.
    """

    def __init__(self):
        super().__init__('arm_planner')
        qos_profile = QoSProfile(depth=10)

        # 카메라 오프셋 설정 (센티미터 단위)
        self.cam_offset = Point(x=0.0, y= -8.0, z= -3.0)  # offset 계산하는법

        # 실세계 좌표를 수신하기 위한 구독자 생성 (CoordTransformer 노드로부터)
        self.world_coord_subscriber = self.create_subscription(
            Point, 
            'world_coordinates', 
            self.world_coord_callback, 
            qos_profile
        )
        self.get_logger().info("Subscribed to 'world_coordinates' topic.")

        # 로봇 팔 좌표를 발행하기 위한 퍼블리셔 생성
        self.robot_point_publisher = self.create_publisher(
            Point,
            'arm_coordinate_commands',
            qos_profile
        )
        self.get_logger().info("Publishing to 'arm_coordinate_commands' topic.")

    def world_coord_callback(self, msg):
        try:
            X = msg.x  # cm 단위
            Y = msg.y  # cm 단위
            Z = msg.z  # cm 단위

            # 카메라 오프셋을 적용하고 mm 단위로 변환
            robot_coord = Point()
            robot_coord.x = (X + self.cam_offset.x) * 10  # cm -> mm 변환
            robot_coord.y = (Y + self.cam_offset.y) * 10
            robot_coord.z = (Z + self.cam_offset.z) * 10

            self.robot_point_publisher.publish(robot_coord)
            self.get_logger().info(f"Published robot coordinates: X={robot_coord.x:.2f} mm, Y={robot_coord.y:.2f} mm, Z={robot_coord.z:.2f} mm")
        except Exception as e:
            self.get_logger().error(f"Error in world_coord_callback: {e}")

def main(args=None):
    rclpy.init(args=args)
    arm_planner = ArmPlanner()
    try:
        rclpy.spin(arm_planner)
    except KeyboardInterrupt:
        arm_planner.get_logger().info("Shutting down ArmPlanner node.")
    finally:
        arm_planner.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main() 
