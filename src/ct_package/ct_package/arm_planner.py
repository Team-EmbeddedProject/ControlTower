import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from geometry_msgs.msg import Point
import time
import logging
from ct_package.cam_coord_transform import CamCoordTransformer, CoordPixel, Coord3D

# CRITICAL, ERROR, WARNING, INFO, DEBUG
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 이미지 좌표계 변환하고 arm_coordinate_commands 토픽으로 퍼블리시 
class ArmPlanner(Node):
    def __init__(self):
        super().__init__('arm_planner')
        qos_profile = QoSProfile(depth=10)
        
        # cam_offset, cam_angle, intrinsic_mat_file, pixel_width, pixel_height 설정
        self.cam_cood_transfomer = CamCoordTransformer(cam_offset=Coord3D(0, 80, 100), cam_angle=141.0)

        # 이미지 좌표
        self.trash_point_subscriber = self.create_subscription(
            Point, 
            'trash_point', 
            self.point_lisener_callback, 
            qos_profile
        )

        # 로봇 팔 좌표
        self.robot_point_publisher = self.create_publisher(
            Point,
            'arm_coordinate_commands',
            qos_profile
        )

    def point_lisener_callback(self, msg):
        try:
            u = int(msg.x)
            v = int(msg.y)
            pixel_coord = CoordPixel(u, v)
            target_z = msg.z #  mm
            world_coord = self.cam_cood_transfomer.pixel_to_world_coord(pixel_coord, target_z)

            robot_coord = Point()
            robot_coord.x = world_coord.x + (self.cam_cood_transfomer.cam_offset.y / 10)
            robot_coord.y = world_coord.y + (self.cam_cood_transfomer.cam_offset.y / 10) + (self.cam_cood_transfomer.cam_offset.z / 10)
            robot_coord.z = world_coord.z + 4

            self.robot_point_publisher.publish(robot_coord)
            self.get_logger().info(f"Published robot coordinates: {robot_coord}")
        except Exception as e:
            self.get_logger().error(f"Error in point_listener_callback: {e}")

def main(args=None):
    rclpy.init(args=args)
    arm_planner = ArmPlanner()
    rclpy.spin(arm_planner)
    arm_planner.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
