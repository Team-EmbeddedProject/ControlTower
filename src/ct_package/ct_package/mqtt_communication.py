import rclpy
from rclpy.node import Node
#import paho.mqtt.client as mqtt
#import ssl
from interface_package.msg import RobotLog
from interface_package.srv import TrashInfo

# AWS IoT Core - Connect, Disconnet 하는 함수 생성
# MQTT 프로토콜로 전송하는 함수
class MqttCommunication(Node):
    def __init__(self):
        super().__init__('mqtt_communication')


        #AWS Iot Core 엔드포인트 설정
        
        self.trash_info_server = self.create_service(TrashInfo, 'trash_detection', self.trash_detection_callback)
        self.log_subscriber = self.create_subscription(RobotLog, 'robot_log', self.robot_log_callback, 10)
        self.get_logger().info('MQTT Communication start')
    
    def trash_detection_callback(self, request, response):
        # AWS IoT Core에 Trash Data 저장하는 코드 작성
        # 성공하면 response.success = True 반환, 실패하면 Fasle
        response.success = True
        self.get_logger().info(f'Request Data - {request.timestamp} {request.robot_id} {request.trash_type} {request.trash_location}')
        return response

    def robot_log_callback(self, msg):
        # AWS IoT Core에 Robot Log 저장하는 코드 작성
        self.get_logger().info(f'Subscribe Data: {msg.timestamp} {msg.robot_id} {msg.robot_location} {msg.status}')

def customCallback(client, userdata, message):
    print("receivced a new messsage: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print ("----------\n")

def main(args=None):
    rclpy.init(args=args)
    mqtt_communication = MqttCommunication()
    try:
        rclpy.spin(mqtt_communication)
    except KeyboardInterrupt:
        pass
    finally:
        mqtt_communication.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
