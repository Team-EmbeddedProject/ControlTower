import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import LifecycleNode
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration, Command

def generate_launch_description():
    param_file_dir = os.path.join(
        get_package_share_directory('ct_package'),
        'params',
        'mqtt_param.yaml'
    )

    return LaunchDescription([
        Node(
            package='ct_package',
            executable='mqtt_communication',
            name='mqtt_communication',
            output='screen',
            parameters=[param_file_dir]
        ),

        Node(
            package='ct_package',
            executable='arm_planner',
            name='arm_planner',
            output='screen'
        ),

        Node(
            package='ct_package',
            executable='trash_detector',
            name='trash_detector',
            output='screen'
        )
    ])
