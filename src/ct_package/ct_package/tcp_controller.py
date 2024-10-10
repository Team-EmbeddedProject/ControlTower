from socket import *
import threading
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
from interface_package.srv import ModeNum

# 서버 설정
host = "0.0.0.0"
port = 3000

class TcpController(Node):
    def __init__(self):
        super().__init__('tcp_controller')
        self.client = self.create_client(ModeNum, 'change_mode')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service...')

        self.cmd_vel_publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.create_socket()
        self.get_logger().info("TCP server is running and listening...")

    def create_socket(self):
        # 소켓 생성
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        self.serverSocket.bind((host, port))
        self.serverSocket.listen(100)
        # 클라이언트 접속을 위한 스레드 처리
        threading.Thread(target=self.accept_clients, daemon=True).start()

    def accept_clients(self):
        while True:
            try:
                connectionSocket, addr = self.serverSocket.accept()
                client_thread = threading.Thread(target=self.handle_client, args=(connectionSocket, addr))
                client_thread.start()
            except Exception as e:
                self.get_logger().error(f"Server error: {e}")
                break
        self.serverSocket.close()

    def handle_client(self, connectionSocket, addr):
        # -- 통신 코드--
        # 000: 통신 종료 
        # 100: 자동 모드 / 200: 원격 제어 모드
        # 301: 홈으로 돌아가기 / 302: 강제 종료
        # 400: 정지 / 401: 이동(전) / 402: 이동(후) / 403: 좌회전 / 404: 우회전
        self.get_logger().info(f"[{addr}] connected")
        # mode change
        try:
            while True:
                data = connectionSocket.recv(1024)
                if not data:
                    break
                command = data.decode("utf-8").strip()
                self.get_logger().info(f"[{addr}] received: {command}")

                if command == "100":
                    self.send_request(100)
                elif command == "200":
                    self.send_request(200)
                
                # Twist 메시지 생성 및 전송 로직
                if command in ["400", "401", "402", "403", "404"]:
                    twist = Twist()
                    if command == "400": # 정지
                        twist.linear.x = 0.0
                        twist.angular.z = 0.0
                    elif command == "401":  # 전진
                        twist.linear.x = 0.5
                    elif command == "402":  # 후진
                        twist.linear.x = -0.5
                    elif command == "403":  # 좌회전
                        twist.angular.z = 0.4
                    elif command == "404":  # 우회전
                        twist.angular.z = -0.4
                    self.cmd_vel_publisher.publish(twist)
                    self.get_logger().info(f"Publishing command to robot: {twist}")

                # 클라이언트에게 응답 보내기
                connectionSocket.send(f"Executed command: {command}".encode("utf-8"))

                if command == "000":  # 종료 명령
                    break
        finally:
            connectionSocket.close()
            self.send_request(100)
            self.get_logger().info(f"[{addr}] disconnected")

    def send_request(self, mode):
        request = ModeNum.Request()
        request.mode = mode
        future = self.client.call_async(request)
        future.add_done_callback(self.handle_response)

    def handle_response(self, future):
        try:
            response = future.result()
            if response is not None:
                self.get_logger().info(f"Service call succeeded: {response}")
            else:
                self.get_logger().error("Service call failed.")
        except Exception as e:
            self.get_logger().error(f"Service call exception: {str(e)}")

def main(args=None):
    rclpy.init(args=args)
    tcp_controller = TcpController()

    try:
        rclpy.spin(tcp_controller)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            tcp_controller.destroy_node()
            rclpy.shutdown()

if __name__ == '__main__':
    main()

