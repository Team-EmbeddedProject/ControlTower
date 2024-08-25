# import rclpy
# from rclpy.node import Node
# #import paho.mqtt.client as mqtt
# #import ssl
# from interface_package.msg import RobotLog
# from interface_package.srv import TrashInfo

# # AWS IoT Core - Connect, Disconnet 하는 함수 생성
# # MQTT 프로토콜로 전송하는 함수
# class MqttCommunication(Node):
#     def __init__(self):
#         super().__init__('mqtt_communication')


#         #AWS Iot Core 엔드포인트 설정
        
#         self.trash_info_server = self.create_service(TrashInfo, 'trash_detection', self.trash_detection_callback)
#         self.log_subscriber = self.create_subscription(RobotLog, 'robot_log', self.robot_log_callback, 10)
#         self.get_logger().info('MQTT Communication start')
    
#     def trash_detection_callback(self, request, response):
#         # AWS IoT Core에 Trash Data 저장하는 코드 작성
#         # 성공하면 response.success = True 반환, 실패하면 Fasle
#         response.success = True
#         self.get_logger().info(f'Request Data - {request.timestamp} {request.robot_id} {request.trash_type} {request.trash_location}')
#         return response

#     def robot_log_callback(self, msg):
#         # AWS IoT Core에 Robot Log 저장하는 코드 작성
#         self.get_logger().info(f'Subscribe Data: {msg.timestamp} {msg.robot_id} {msg.robot_location} {msg.status}')

# def customCallback(client, userdata, message):
#     print("receivced a new messsage: ")
#     print(message.payload)
#     print("from topic: ")
#     print(message.topic)
#     print ("----------\n")

# def main(args=None):
#     rclpy.init(args=args)
#     mqtt_communication = MqttCommunication()
#     try:
#         rclpy.spin(mqtt_communication)
#     except KeyboardInterrupt:
#         pass
#     finally:
#         mqtt_communication.destroy_node()
#         rclpy.shutdown()

# if __name__ == '__main__':
#     main()

from awsiot import mqtt5_client_builder
from awscrt import mqtt5, http
import threading
from concurrent.futures import Future
import time
import json
import rclpy
from rclpy.node import Node
from ct_package.command_line_utils import CommandLineUtils
from interface_package.msg import RobotLog
from interface_package.srv import TrashInfo

TIMEOUT = 100
topic_filter = "test/topic"

class MqttCommunication(Node):
    def __init__(self):
        super().__init__('mqtt_communication')

        # ROS 2 Service and Subscriber
        self.trash_info_server = self.create_service(TrashInfo, 'trash_detection', self.trash_detection_callback)
        self.log_subscriber = self.create_subscription(RobotLog, 'robot_log', self.robot_log_callback, 10)
        self.get_logger().info('MQTT Communication start')

        # Initialize MQTT
        self.cmdData = CommandLineUtils.parse_sample_input_mqtt5_pubsub()
        self.received_count = 0
        self.received_all_event = threading.Event()
        self.future_stopped = Future()
        self.future_connection_success = Future()

        self.setup_mqtt_client()

    def setup_mqtt_client(self):
        proxy_options = None
        if self.cmdData.input_proxy_host is not None and self.cmdData.input_proxy_port != 0:
            proxy_options = http.HttpProxyOptions(
                host_name=self.cmdData.input_proxy_host,
                port=self.cmdData.input_proxy_port)

        # Create MQTT5 client
        self.client = mqtt5_client_builder.mtls_from_path(
            endpoint=self.cmdData.input_endpoint,
            port=self.cmdData.input_port,
            cert_filepath=self.cmdData.input_cert,
            pri_key_filepath=self.cmdData.input_key,
            ca_filepath=self.cmdData.input_ca,
            http_proxy_options=proxy_options,
            on_publish_received=self.on_publish_received,
            on_lifecycle_stopped=self.on_lifecycle_stopped,
            on_lifecycle_connection_success=self.on_lifecycle_connection_success,
            on_lifecycle_connection_failure=self.on_lifecycle_connection_failure,
            client_id=self.cmdData.input_clientId)

        self.client.start()
        lifecycle_connect_success_data = self.future_connection_success.result(TIMEOUT)
        connack_packet = lifecycle_connect_success_data.connack_packet

        if not self.cmdData.input_is_ci:
            self.get_logger().info(
                f"Connected to endpoint:'{self.cmdData.input_endpoint}' with Client ID:'{self.cmdData.input_clientId}' with reason_code:{repr(connack_packet.reason_code)}")

        self.subscribe_to_topic(self.cmdData.input_topic)

    def subscribe_to_topic(self, topic):
        self.get_logger().info(f"Subscribing to topic '{topic}'...")
        subscribe_future = self.client.subscribe(subscribe_packet=mqtt5.SubscribePacket(
            subscriptions=[mqtt5.Subscription(
                topic_filter=topic,
                qos=mqtt5.QoS.AT_LEAST_ONCE)]
        ))
        suback = subscribe_future.result(TIMEOUT)
        self.get_logger().info(f"Subscribed with {suback.reason_codes}")

    def on_publish_received(self, publish_packet_data):
        publish_packet = publish_packet_data.publish_packet
        assert isinstance(publish_packet, mqtt5.PublishPacket)
        self.get_logger().info(f"Received message from topic '{publish_packet.topic}': {publish_packet.payload}")
        self.received_count += 1
        if self.received_count == self.cmdData.input_count:
            self.received_all_event.set()

    def on_lifecycle_stopped(self, lifecycle_stopped_data: mqtt5.LifecycleStoppedData):
        self.get_logger().info("Lifecycle Stopped")
        self.future_stopped.set_result(lifecycle_stopped_data)

    def on_lifecycle_connection_success(self, lifecycle_connect_success_data: mqtt5.LifecycleConnectSuccessData):
        self.get_logger().info("Lifecycle Connection Success")
        self.future_connection_success.set_result(lifecycle_connect_success_data)

    def on_lifecycle_connection_failure(self, lifecycle_connection_failure: mqtt5.LifecycleConnectFailureData):
        self.get_logger().info(f"Lifecycle Connection Failure: {lifecycle_connection_failure.exception}")

    def trash_detection_callback(self, request, response):
        # Publish Trash Info to AWS IoT Core
        message = {
            "timestamp": str(request.timestamp),
            "robot_id": request.robot_id,
            "trash_type": request.trash_type,
            "trash_location": request.trash_location
        }
        self.publish_to_mqtt(json.dumps(message))
        response.success = True
        self.get_logger().info(f'Published TrashInfo Data - {message}')
        return response

    def robot_log_callback(self, msg):
        # Publish Robot Log to AWS IoT Core
        message = {
            "timestamp": str(msg.timestamp),
            "robot_id": msg.robot_id,
            "robot_location": msg.robot_location,
            "status": msg.status
        }
        self.publish_to_mqtt(json.dumps(message))
        self.get_logger().info(f'Published RobotLog Data - {message}')

    def publish_to_mqtt(self, message):
        self.get_logger().info(f"Publishing message to topic '{self.cmdData.input_topic}': {message}")
        publish_future = self.client.publish(mqtt5.PublishPacket(
            topic=self.cmdData.input_topic,
            payload=message.encode('utf-8'),
            qos=mqtt5.QoS.AT_LEAST_ONCE
        ))
        publish_completion_data = publish_future.result(TIMEOUT)
        self.get_logger().info(f"PubAck received with {repr(publish_completion_data.puback.reason_code)}")

    def stop_client(self):
        self.client.stop()
        self.future_stopped.result(TIMEOUT)
        self.get_logger().info("MQTT Client Stopped!")

def main(args=None):
    rclpy.init(args=args)
    mqtt_communication = MqttCommunication()
    try:
        rclpy.spin(mqtt_communication)
    except KeyboardInterrupt:
        pass
    finally:
        mqtt_communication.stop_client()
        mqtt_communication.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
