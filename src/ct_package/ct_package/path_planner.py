from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from rclpy.node import Node
from rclpy.duration import Duration

import math
from time import sleep
from collections import namedtuple

Position = namedtuple('Position', ['x', 'y'])

# goal poses를 navigation followWaypoints의 인자로 전달
# point에 도달할 때마다 로봇 로그 전달
# 
# 수동 제어로 바뀌는 경우, 쓰레기를 발견한 경우 고려
class PathPlanner(Node):
    def __init__(self):
        super().__init__("path_planner")

        self.nav = BasicNavigator()

        # 초기 위치 설정
        self.initial_pose = PoseStamped()
        self.initial_pose.header.frame_id = 'map'
        self.initial_pose.header.stamp = self.get_clock().now().to_msg()
        self.initial_pose.pose.position.x = 0.0
        self.initial_pose.pose.position.y = 0.0
        self.initial_pose.pose.orientation.z = 0.0
        self.initial_pose.pose.orientation.w = 1.0
        self.nav.setInitialPose(initial_pose)

        self.nav.waitUntilNav2Active()

        self.goal_poses = []
        self.set_goal_poses()
        self.follow_waypoints()

    def parse_points(self, points_str):
        """YAML 파일로부터 받은 points 파라미터를 파싱하여 (x, y) 좌표 리스트로 반환"""
        positions = []
        for point in points_str.split(';'):
            if point.strip():  # 빈 줄 제외
                key_value = point.split(':')
                coords = [float(coord.strip()) for coord in key_value[1].split(',')]
                positions.append(Position(coords[0], coords[1]))  # (x, y) 좌표를 Position으로 추가
        return positions
    
    def set_goal_poses(self):
        self.declare_parameter("points", "")
        points_str = self.get_parameter("points").get_parameter_value().string_value
        self.positions = self.parse_points(points_str)
        
        for i, position in enumerate(self.positions):
            goal_pose = PoseStamped()
            goal_pose.header.frame_id = 'map'
            goal_pose.header.stamp = self.get_clock().now().to_msg()
            goal_pose.pose.position.x = position.x
            goal_pose.pose.position.y = position.y
            goal_pose.pose.orientation.w = 1.0
            goal_pose.pose.orientation.z = 0.0
            self.goal_poses.append(goal_pose)
            self.get_logger().info(f"Goal {i+1} set: {position.x}, {position.y}")

    def follow_waypoints(self):
        nav_start = nav.get_clock().now()
        self.nav.followWaypoints(self.goal_poses)

        i = 0
        last_waypoint = -1  # 마지막으로 도착한 waypoint를 저장하는 변수
        while not self.nav.isTaskComplete():
            # Do something with the feedback
            i = i + 1
            feedback = self.nav.getFeedback()
            if feedback and i % 10 == 0: # 1초마다
                print(
                    'Executing current waypoint: '
                    + str(feedback.current_waypoint + 1)
                    + '/'
                    + str(len(self.goal_poses))
                )

                # waypoint에 도착했는지 확인
                if feedback.current_waypoint != last_waypoint:
                    last_waypoint = feedback.current_waypoint

                    # Waypoint에 도착할 때 신호 (로그 출력)
                    self.get_logger().info(
                        f"Arrived at waypoint {feedback.current_waypoint + 1}: "
                        f"x = {self.goal_poses[feedback.current_waypoint].pose.position.x}, "
                        f"y = {self.goal_poses[feedback.current_waypoint].pose.position.y}"
                    )

                now = self.get_clock().now()

                # Some navigation timeout to demo cancellation
                if now - nav_start > Duration(seconds=600.0):
                    self.nav.cancelTask()

        result = self.nav.getResult()
        if result == TaskResult.SUCCEEDED:
            print('Goal succeeded!')
        elif result == TaskResult.CANCELED:
            print('Goal was canceled!')
        elif result == TaskResult.FAILED:
            print('Goal failed!')
        else:
            print('Goal has an invalid return status!')

        self.nav.lifecycleShutdown() 

def main(args=None):
    rclpy.init(args=args)
    path_planner = PathPlanner()
    try:
        rclpy.spin(path_planner)  # 노드 스핀 (실행)
    except KeyboardInterrupt:
        print("Shutting down...")  # 종료 메시지 출력
    finally:
        if rclpy.ok():
            path_planner.destroy_node()
            rclpy.shutdown()

if __name__ == '__main__':
    main()