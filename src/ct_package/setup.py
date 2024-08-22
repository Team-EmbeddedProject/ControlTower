from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'ct_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'params'), glob('params/*.yaml'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pi',
    maintainer_email='pi@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'camera_subscriber = ct_package.camera_subscriber:main',
            'trash_detector = ct_package.trash_detector:main',
            'data_publisher = ct_package.data_publisher:main',
            'mqtt_communication = ct_package.mqtt_communication:main',
            'camera_calibration = ct_package.camera_calibration:main',
            'arm_planner = ct_package.arm_planner:main',
            'cam_coord_transform = ct_package.cam_coord_transform:main'
        ],
    },
    package_data={
        package_name: [
            'launch/*.launch.py',
            'maps/*',
        ],
    },
    include_package_data=True,
)
