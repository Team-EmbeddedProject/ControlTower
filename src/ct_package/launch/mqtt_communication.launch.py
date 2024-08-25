import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Get the directory where the parameter file is stored
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
        )
    ])