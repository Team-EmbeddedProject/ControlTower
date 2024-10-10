import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_package',
            executable='sensor_processing',
            name='sensor_processing',
            output='screen'
        ),

        Node(
            package='robot_package',
            executable='arm_controller',
            name='arm_controller',
            output='screen'
        ),

        Node(
            package='ct_package',
            executable='arm_planner',
            name='arm_planner',
            output='screen'
        ),

        Node(
            package='ct_package',
            executable='cam_coord_transform',
            name='cam_coord_transform',
            output='screen'
        ),

        Node(
            package='ct_package',
            executable='trash_detector',
            name='trash_detector',
            output='screen'
        )
    ])
