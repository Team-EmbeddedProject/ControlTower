# from awsiot import mqtt5_client_builder
# from awscrt import mqtt5, http
# import threading
# from concurrent.futures import Future
# import time
# from datetime import datetime
# from zoneinfo import ZoneInfo
# import json
# import rclpy
# from rclpy.node import Node
# #from interface_package.msg import RobotLog
# from interface_package.srv import TrashInfo, RobotLog

# TIMEOUT = 100

# class MqttCommunication(Node):
#     def __init__(self):
#         super().__init__('mqtt_communication')

#         # ROS 2 Service and Subscriber
#         self.trash_info_server = self.create_service(TrashInfo, 'trash_detection', self.trash_detection_callback)
#         self.log_subscriber = self.create_subscription(RobotLog, 'robot_log', self.robot_log_callback,10)
#         self.get_logger().info('MQTT Communication start')
        
#         # Initialize parameters
#         self.declare_parameters(
#             namespace='',
#             parameters=[
#                 ('input_endpoint', ''),
#                 ('input_port', 0),
#                 ('input_cert', ''),
#                 ('input_key', ''),
#                 ('input_ca', ''),
#                 ('input_clientId', ''),
#                 ('trash_info_topic', ''),
#                 ('robot_log_topic', ''),
#                 ('input_count', 0),
#                 ('input_proxy_host', ''),
#                 ('input_proxy_port', 0),
#                 ('input_is_ci', False),
#             ]
#         )

#         # Initialize MQTT
#         self.cmdData = self.get_cmd_data_from_parameters()
#         self.received_count = 0
#         self.received_all_event = threading.Event()
#         self.future_stopped = Future()
#         self.future_connection_success = Future()

#         self.setup_mqtt_client()

#     def get_cmd_data_from_parameters(self):
#         cmdData = type('', (), {})()  # Create an empty object to hold attributes
#         cmdData.input_endpoint = self.get_parameter('input_endpoint').get_parameter_value().string_value
#         cmdData.input_port = self.get_parameter('input_port').get_parameter_value().integer_value
#         cmdData.input_cert = self.get_parameter('input_cert').get_parameter_value().string_value
#         cmdData.input_key = self.get_parameter('input_key').get_parameter_value().string_value
#         cmdData.input_ca = self.get_parameter('input_ca').get_parameter_value().string_value
#         cmdData.input_clientId = self.get_parameter('input_clientId').get_parameter_value().string_value
#         cmdData.trash_info_topic = self.get_parameter('trash_info_topic').get_parameter_value().string_value
#         cmdData.robot_log_topic = self.get_parameter('robot_log_topic').get_parameter_value().string_value
#         cmdData.input_count = self.get_parameter('input_count').get_parameter_value().integer_value
#         cmdData.input_proxy_host = self.get_parameter('input_proxy_host').get_parameter_value().string_value
#         cmdData.input_proxy_port = self.get_parameter('input_proxy_port').get_parameter_value().integer_value
#         cmdData.input_is_ci = self.get_parameter('input_is_ci').get_parameter_value().bool_value
#         return cmdData

#     def setup_mqtt_client(self):
#         proxy_options = None
#         if self.cmdData.input_proxy_host is not None and self.cmdData.input_proxy_port != 0:
#             proxy_options = http.HttpProxyOptions(
#                 host_name=self.cmdData.input_proxy_host,
#                 port=self.cmdData.input_proxy_port)

#         # Create MQTT5 client
#         self.client = mqtt5_client_builder.mtls_from_path(
#             endpoint=self.cmdData.input_endpoint,
#             port=self.cmdData.input_port,
#             cert_filepath=self.cmdData.input_cert,
#             pri_key_filepath=self.cmdData.input_key,
#             ca_filepath=self.cmdData.input_ca,
#             http_proxy_options=proxy_options,
#             on_publish_received=self.on_publish_received,
#             on_lifecycle_stopped=self.on_lifecycle_stopped,
#             on_lifecycle_connection_success=self.on_lifecycle_connection_success,
#             on_lifecycle_connection_failure=self.on_lifecycle_connection_failure,
#             client_id=self.cmdData.input_clientId)

#         self.client.start()
#         lifecycle_connect_success_data = self.future_connection_success.result(TIMEOUT)
#         connack_packet = lifecycle_connect_success_data.connack_packet

#         if not self.cmdData.input_is_ci:
#             self.get_logger().info(
#                 f"Connected to endpoint:'{self.cmdData.input_endpoint}' with Client ID:'{self.cmdData.input_clientId}' with reason_code:{repr(connack_packet.reason_code)}")

#     def subscribe_to_topic(self, topic):
#         self.get_logger().info(f"Subscribing to topic '{topic}'...")
#         subscribe_future = self.client.subscribe(subscribe_packet=mqtt5.SubscribePacket(
#             subscriptions=[mqtt5.Subscription(
#                 topic_filter=topic,
#                 qos=mqtt5.QoS.AT_LEAST_ONCE)]
#         ))
#         suback = subscribe_future.result(TIMEOUT)
#         self.get_logger().info(f"Subscribed with {suback.reason_codes}")

#     def on_publish_received(self, publish_packet_data):
#         publish_packet = publish_packet_data.publish_packet
#         assert isinstance(publish_packet, mqtt5.PublishPacket)
#         self.get_logger().info(f"Received message from topic '{publish_packet.topic}': {publish_packet.payload}")
#         self.received_count += 1
#         if self.received_count == self.cmdData.input_count:
#             self.received_all_event.set()

#     def on_lifecycle_stopped(self, lifecycle_stopped_data: mqtt5.LifecycleStoppedData):
#         self.get_logger().info("Lifecycle Stopped")
#         self.future_stopped.set_result(lifecycle_stopped_data)

#     def on_lifecycle_connection_success(self, lifecycle_connect_success_data: mqtt5.LifecycleConnectSuccessData):
#         self.get_logger().info("Lifecycle Connection Success")
#         if not self.future_connection_success.done():
#             self.future_connection_success.set_result(lifecycle_connect_success_data)

#     def on_lifecycle_connection_failure(self, lifecycle_connection_failure: mqtt5.LifecycleConnectFailureData):
#         self.get_logger().info(f"Lifecycle Connection Failure: {lifecycle_connection_failure.exception}")

#     def trash_detection_callback(self, request, response):
#         # Publish Trash Info to AWS IoT Core
#         mysql_timestamp = datetime.fromtimestamp(
#             request.timestamp.sec + request.timestamp.nanosec * 1e-9,
#             tz=ZoneInfo("Asia/Seoul")
#             ).strftime('%Y-%m-%d %H:%M:%S')
        
#         message = {
#             "timestamp": mysql_timestamp,
#             "robot_id": request.robot_id,
#             "trash_type": request.trash_type,
#             "latitude": float(request.latitude),
#             "longitude": float(request.longitude)
#         }
#         self.publish_to_mqtt(json.dumps(message), self.cmdData.trash_info_topic)
#         response.success = True
#         self.get_logger().info(f'Published TrashInfo Data - {message}')
#         return response

#     def robot_log_callback(self, msg):
#         # Publish Robot Log to AWS IoT Core
#         mysql_timestamp = datetime.fromtimestamp(
#             msg.timestamp.sec + msg.timestamp.nanosec * 1e-9,
#             tz=ZoneInfo("Asia/Seoul")
#             ).strftime('%Y-%m-%d %H:%M:%S')

#         message = {
#             "timestamp": mysql_timestamp,
#             "row_id": msg.row_id,
#             "col_id": msg.col_id,
#         }
#         self.publish_to_mqtt(json.dumps(message), self.cmdData.robot_log_topic)
#         self.get_logger().info(f'Published RobotLog Data - {message}')

#     def publish_to_mqtt(self, message, input_topic):
#         self.get_logger().info(f"Publishing message to topic '{input_topic}': {message}")
#         publish_future = self.client.publish(mqtt5.PublishPacket(
#             topic=input_topic,
#             payload=message.encode('utf-8'),
#             qos=mqtt5.QoS.AT_LEAST_ONCE
#         ))
#         publish_completion_data = publish_future.result(TIMEOUT)
#         self.get_logger().info(f"PubAck received with {repr(publish_completion_data.puback.reason_code)}")

#     def stop_client(self):
#         self.client.stop()
#         self.future_stopped.result(TIMEOUT)
#         self.get_logger().info("MQTT Client Stopped!")

# def main(args=None):
#     rclpy.init(args=args)
#     mqtt_communication = MqttCommunication()
#     try:
#         rclpy.spin(mqtt_communication)
#     except KeyboardInterrupt:
#         pass
#     finally:
#         mqtt_communication.stop_client()
#         mqtt_communication.destroy_node()
#         rclpy.shutdown()

# if __name__ == '__main__':
#     main()

from awsiot import mqtt5_client_builder
from awscrt import mqtt5, http
import threading
from concurrent.futures import Future
import time
from datetime import datetime
from zoneinfo import ZoneInfo
import json
import rclpy
from rclpy.node import Node
from interface_package.msg import RobotLog  # RobotLog를 메시지로 가져옵니다
from interface_package.srv import TrashInfo  # TrashInfo는 여전히 서비스로 유지

TIMEOUT = 100

class MqttCommunication(Node):
    def __init__(self):
        super().__init__('mqtt_communication')

        # ROS 2 Service and Subscriber
        self.trash_info_server = self.create_service(TrashInfo, 'trash_detection', self.trash_detection_callback)
        self.log_subscriber = self.create_subscription(RobotLog, 'robot_log', self.robot_log_callback, 10)  # RobotLog 메시지 구독자로 변경
        self.get_logger().info('MQTT Communication start')

        # Initialize parameters
        self.declare_parameters(
            namespace='',
            parameters=[
                ('input_endpoint', ''),
                ('input_port', 0),
                ('input_cert', ''),
                ('input_key', ''),
                ('input_ca', ''),
                ('input_clientId', ''),
                ('trash_info_topic', ''),
                ('robot_log_topic', ''),
                ('input_count', 0),
                ('input_proxy_host', ''),
                ('input_proxy_port', 0),
                ('input_is_ci', False),
            ]
        )

        # Initialize MQTT
        self.cmdData = self.get_cmd_data_from_parameters()
        self.received_count = 0
        self.received_all_event = threading.Event()
        self.future_stopped = Future()
        self.future_connection_success = Future()

        self.setup_mqtt_client()

    def get_cmd_data_from_parameters(self):
        cmdData = type('', (), {})()  # Create an empty object to hold attributes
        cmdData.input_endpoint = self.get_parameter('input_endpoint').get_parameter_value().string_value
        cmdData.input_port = self.get_parameter('input_port').get_parameter_value().integer_value
        cmdData.input_cert = self.get_parameter('input_cert').get_parameter_value().string_value
        cmdData.input_key = self.get_parameter('input_key').get_parameter_value().string_value
        cmdData.input_ca = self.get_parameter('input_ca').get_parameter_value().string_value
        cmdData.input_clientId = self.get_parameter('input_clientId').get_parameter_value().string_value
        cmdData.trash_info_topic = self.get_parameter('trash_info_topic').get_parameter_value().string_value
        cmdData.robot_log_topic = self.get_parameter('robot_log_topic').get_parameter_value().string_value
        cmdData.input_count = self.get_parameter('input_count').get_parameter_value().integer_value
        cmdData.input_proxy_host = self.get_parameter('input_proxy_host').get_parameter_value().string_value
        cmdData.input_proxy_port = self.get_parameter('input_proxy_port').get_parameter_value().integer_value
        cmdData.input_is_ci = self.get_parameter('input_is_ci').get_parameter_value().bool_value
        return cmdData

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
        if not self.future_connection_success.done():
            self.future_connection_success.set_result(lifecycle_connect_success_data)

    def on_lifecycle_connection_failure(self, lifecycle_connection_failure: mqtt5.LifecycleConnectFailureData):
        self.get_logger().info(f"Lifecycle Connection Failure: {lifecycle_connection_failure.exception}")

    # TrashInfo 서비스 콜백 함수
    def trash_detection_callback(self, request, response):
        # Publish Trash Info to AWS IoT Core
        mysql_timestamp = datetime.fromtimestamp(
            request.timestamp.sec + request.timestamp.nanosec * 1e-9,
            tz=ZoneInfo("Asia/Seoul")
        ).strftime('%Y-%m-%d %H:%M:%S')

        message = {
            "timestamp": mysql_timestamp,
            "robot_id": request.robot_id,
            "trash_type": request.trash_type,
            "latitude": float(request.latitude),
            "longitude": float(request.longitude)
        }
        self.publish_to_mqtt(json.dumps(message), self.cmdData.trash_info_topic)
        response.success = True
        self.get_logger().info(f'Published TrashInfo Data - {message}')
        return response

    # RobotLog 메시지 구독자 콜백 함수
    def robot_log_callback(self, msg):
        # Publish Robot Log to AWS IoT Core
        self.get_logger().info(f'Received RobotLog message: {msg}')
        mysql_timestamp = datetime.fromtimestamp(
            msg.timestamp.sec + msg.timestamp.nanosec * 1e-9,
            tz=ZoneInfo("Asia/Seoul")
        ).strftime('%Y-%m-%d %H:%M:%S')

        message = {
            "timestamp": mysql_timestamp,
            "robot_id": msg.robot_id,
            "row_id": msg.row_id,
            "col_id": msg.col_id,
        }
        self.publish_to_mqtt(json.dumps(message), self.cmdData.robot_log_topic)
        self.get_logger().info(f'Published RobotLog Data - {message}')

    def publish_to_mqtt(self, message, input_topic):
        self.get_logger().info(f"Publishing message to topic '{input_topic}': {message}")
        publish_future = self.client.publish(mqtt5.PublishPacket(
            topic=input_topic,
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
