import rclpy
from rclpy.node import Node
import cv2
import numpy as np
import glob
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Point

class PixelToWorldConverter:

    # 2D 픽셀 좌표를 실제 3D 세계 좌표로 변환하는 클래스.
    # Attributes:
    #     intrinsic_matrix (np.ndarray): 카메라의 내부 행렬 (3x3).
    #     fx (float): 카메라의 x축 초점 거리.
    #     fy (float): 카메라의 y축 초점 거리.
    #     cx (float): 이미지의 x축 주점 (principal point).
    #     cy (float): 이미지의 y축 주점 (principal point).
    #     dist_coeffs (np.ndarray): 카메라의 왜곡 계수.


    def __init__(self, intrinsic_matrix=None, dist_coeffs=None):

        # PixelToWorldConverter 클래스의 생성자.

        # Args:
        #     intrinsic_matrix (np.ndarray, optional): 카메라의 내부 행렬 (3x3).
        #     dist_coeffs (np.ndarray, optional): 카메라의 왜곡 계수.

        if intrinsic_matrix is not None:
            self.set_intrinsic_matrix(intrinsic_matrix, dist_coeffs)
        else:
            self.intrinsic_matrix = None
            self.fx = None
            self.fy = None
            self.cx = None
            self.cy = None
            self.dist_coeffs = None

    def set_intrinsic_matrix(self, intrinsic_matrix, dist_coeffs):
  
        # 카메라의 내부 행렬과 왜곡 계수를 설정하고 관련 파라미터를 추출합니다.

        # Args:
        #     intrinsic_matrix (np.ndarray): 카메라의 내부 행렬 (3x3).
        #     dist_coeffs (np.ndarray): 카메라의 왜곡 계수.

        self.intrinsic_matrix = intrinsic_matrix
        self.dist_coeffs = dist_coeffs
        self.fx = self.intrinsic_matrix[0, 0]
        self.fy = self.intrinsic_matrix[1, 1]
        self.cx = self.intrinsic_matrix[0, 2]
        self.cy = self.intrinsic_matrix[1, 2]
        print(f"Intrinsic Matrix Set:\n{self.intrinsic_matrix}")
        print(f"Distortion Coefficients Set:\n{self.dist_coeffs}")

    def shift_origin(self, x, y):

        # 픽셀 좌표의 원점을 주점(cx, cy)으로 이동.

        # Args:
        #     x (float or np.ndarray): 픽셀의 x좌표.
        #     y (float or np.ndarray): 픽셀의 y좌표.

        # Returns:
        #     tuple: 원점이 이동된 좌표 (x', y').

        x_shifted = x - self.cx
        y_shifted = y - self.cy
        return x_shifted, y_shifted

    def normalize(self, x_shifted, y_shifted):

        # 이동된 좌표를 초점 거리로 정규화.

        # Args:
        #     x_shifted (float or np.ndarray): 원점이 이동된 x좌표.
        #     y_shifted (float or np.ndarray): 원점이 이동된 y좌표.

        # Returns:
        #     tuple: 정규화된 좌표 (x_normalized, y_normalized).

        x_normalized = x_shifted / self.fx
        y_normalized = y_shifted / self.fy
        return x_normalized, y_normalized

    def apply_depth(self, x_normalized, y_normalized, Z):

        # 정규화된 좌표에 깊이 값을 적용하여 3D 실세계 좌표를 계산.

        # Args:
        #     x_normalized (float or np.ndarray): 정규화된 x좌표.
        #     y_normalized (float or np.ndarray): 정규화된 y좌표.
        #     Z (float): 깊이 값.

        # Returns:
        #     tuple: 실세계 3D 좌표 (X, Y, Z).

        X = x_normalized * Z
        Y = y_normalized * Z
        X += self.offset_x
        Y += self.offset_y
        
        return X, Y, Z

    def pixel_to_world(self, x, y, Z):
        # """
        # 단일 픽셀 좌표와 깊이 값을 실세계 3D 좌표로 변환.

        # Args:
        #     x (float): 픽셀의 x좌표.
        #     y (float): 픽셀의 y좌표.
        #     Z (float): 깊이 값 (cm 단위).

        # Returns:
        #     tuple: 실세계 3D 좌표 (X, Y, Z).
        # """
        if self.intrinsic_matrix is None or self.dist_coeffs is None:
            raise ValueError("Intrinsic matrix or distortion coefficients are not set.")

        # 왜곡 보정
        undistorted_point = cv2.undistortPoints(
            np.array([[x, y]], dtype=np.float32),
            self.intrinsic_matrix,
            self.dist_coeffs,
            P=self.intrinsic_matrix
        )

        # 카메라 좌표계에서의 점 계산
        x_cam = (undistorted_point[0][0][0] - self.cx) / self.fx
        y_cam = (undistorted_point[0][0][1] - self.cy) / self.fy
        z_cam = Z
        print(f"x_cam : {x_cam} y_cam : {y_cam} z_cam : {z_cam}")
        
        # 실세계 3D 좌표 (카메라 프레임 기준)
        X, Y, Z = self.apply_depth(x_cam, y_cam, z_cam)
        print(f"world_x :{X} world_y : {Y} world_z : {Z}")
        return X, Y, Z

class cam_coord_transform(Node):
    # """
    # ROS 2 노드: 카메라 캘리브레이션을 수행하고, 픽셀 좌표를 실세계 3D 좌표로 변환합니다.
    # """

    def __init__(self):
        super().__init__('combined_transform_node')

        # 캘리브레이션 관련 초기화
        self.chessboard_size = (7, 7)  # 체스보드의 내부 코너 개수 (행, 열)
        self.square_size = 3  # 각 사각형의 크기 (단위: cm)

        # 체스보드의 3D 점 (세계 좌표계의 3D 점)
        self.object_points_3d = np.zeros((self.chessboard_size[0] * self.chessboard_size[1], 3), np.float32)
        self.object_points_3d[:, :2] = np.mgrid[0:self.chessboard_size[0], 0:self.chessboard_size[1]].T.reshape(-1, 2)
        self.object_points_3d *= self.square_size  # 실제 크기로 스케일링 (cm 단위)

        # 모든 이미지에서 2D 이미지 포인트와 3D 객체 포인트를 저장할 배열
        self.object_points = []  # 3D 점 (세계 좌표계, cm 단위)
        self.image_points = []  # 2D 점 (이미지 좌표계, 픽셀 단위)

        # 이미지 파일 경로 패턴
        self.image_path_pattern = '/home/pi/workspace/ControlTower/src/ct_package/ct_package/images/*.jpg'  # 실제 이미지 경로로 변경하세요
        self.images = self.load_images(self.image_path_pattern)

        self.image_shape = None  # 이미지 크기를 저장하기 위한 변수

        # 코너 검출의 정확도를 높이기 위한 반복 알고리즘의 종료 기준
        self.criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        # 파라미터 초기화
        self.camera_matrix = None
        self.dist_coeffs = None
        self.rvecs = None
        self.tvecs = None
        self.offset_x = None
        self.offset_y = None
        
        # PixelToWorldConverter 인스턴스 초기화 (초기에는 None)
        self.converter = PixelToWorldConverter()

        # 카메라 보정 수행
        self.read_images_and_find_corners()
        self.calibrate_camera()

        # 이제 PixelToWorldConverter에 intrinsic_matrix와 dist_coeffs를 설정
        if self.camera_matrix is not None and self.dist_coeffs is not None:
            self.converter.set_intrinsic_matrix(self.camera_matrix, self.dist_coeffs)
            self.get_logger().info("PixelToWorldConverter intrinsic_matrix and dist_coeffs set.")
        else:
            self.get_logger().error("Calibration failed. PixelToWorldConverter not set.")

        # 단일 픽셀 좌표를 수신하기 위한 구독자 생성 (trash_detector 노드로부터)
        self.image_subscription = self.create_subscription(
            Point,
            'trash_point',
            self.image_callback,
            10
        )
        self.get_logger().info("Subscribed to 'trash_point' topic.")

        # 월드 좌표를 발행하기 위한 퍼블리셔 생성
        self.world_publisher = self.create_publisher(Point, 'world_coordinates', 10)
        self.get_logger().info("Publishing to 'world_coordinates' topic.")

    def load_images(self, path_pattern):
        # """
        # 주어진 경로 패턴에 맞는 모든 이미지 파일을 읽어 리스트로 반환합니다.
        # """
        image_files = glob.glob(path_pattern)
        if not image_files:
            self.get_logger().error(f"No images found with the pattern: {path_pattern}")
        return image_files

    def read_images_and_find_corners(self):
        # """
        # 이미지 파일을 읽어 체스보드 코너를 검출합니다.
        # """
        for image_file in self.images:
            image = cv2.imread(image_file)
            if image is None:
                self.get_logger().warn(f"Failed to read image: {image_file}")
                continue

            if self.image_shape is None:
                self.image_shape = image.shape[:2][::-1]  # 첫 번째 이미지의 크기를 저장 (width, height)

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            self.find_corners(gray)

    def find_corners(self, gray):
        # """
        # 체스보드에서 코너를 검출하고, 검출된 코너를 저장합니다.
        # """
        ret, corners = cv2.findChessboardCorners(gray, self.chessboard_size, None)

        if ret:
            self.object_points.append(self.object_points_3d)

            # 서브픽셀 정확도로 코너를 찾기
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), self.criteria)
            self.image_points.append(corners2)
            self.get_logger().info("Chessboard corners found and refined.")
        else:
            self.get_logger().warn("Chessboard corners not found in the image.")

    def calibrate_camera(self):

        """
        카메라 보정을 수행하고 결과를 저장하고 발행합니다.
        """
        if not self.object_points or not self.image_points:
            self.get_logger().error("Not enough valid images with detected corners to perform calibration.")
            return

        # 카메라 보정 수행
        ret, self.camera_matrix, self.dist_coeffs, self.rvecs, self.tvecs = cv2.calibrateCamera(
            self.object_points, self.image_points, self.image_shape, None, None)

        if ret:
            self.get_logger().info("Camera calibration successful.")

            # 보정된 카메라 매트릭스 계산
            new_camera_matrix, roi = cv2.getOptimalNewCameraMatrix(
                self.camera_matrix, self.dist_coeffs, self.image_shape, 1, self.image_shape
            )

            # Offset 계산 (보정 전/후 중심 좌표의 차이)
            original_center = (self.camera_matrix[0, 2], self.camera_matrix[1, 2])  # (cx, cy)
            new_center = (new_camera_matrix[0, 2], new_camera_matrix[1, 2])          # (new cx, new cy)

            self.offset_x = new_center[0] - original_center[0]
            self.offset_y = new_center[1] - original_center[1]

            self.get_logger().info(f"Offset (x, y): ({self.offset_x}, {self.offset_y})")

            # 파라미터 발행
            self.publish_parameters()

        else:
            self.get_logger().error("Camera calibration failed.")


    def set_converter_parameters(self):

        # """
        # PixelToWorldConverter에 카메라 보정 파라미터를 설정합니다.
        # """
        if self.camera_matrix is not None and self.dist_coeffs is not None:
            self.converter.set_intrinsic_matrix(self.camera_matrix, self.dist_coeffs)
            self.get_logger().info("PixelToWorldConverter intrinsic_matrix and dist_coeffs set.")
        else:
            self.get_logger().error("Cannot set PixelToWorldConverter parameters due to missing calibration data.")

    def image_callback(self, msg):
        # """
        # 단일 픽셀 좌표를 수신하여 월드 좌표로 변환한 후 발행합니다.

        # Args:
        #     msg (Float32MultiArray): 이미지 좌표 메시지 [u, v].
        # """
        # PixelToWorldConverter가 설정되었는지 확인
        if self.converter.intrinsic_matrix is None or self.converter.dist_coeffs is None:
            self.get_logger().warn("Intrinsic matrix and distortion coefficients not set yet. Ignoring image coordinates.")
            return

        u = msg.x
        v = msg.y
        Z = msg.z  # 깊이 값 (cm)

        try:
            X, Y, Z_world = self.converter.pixel_to_world(u, v, Z)
        except Exception as e:
            self.get_logger().error(f"Error in pixel_to_world conversion: {e}")
            return

        # 실세계 좌표 발행
        world_coord_msg = Point()
        world_coord_msg.x = X
        world_coord_msg.y = Y
        world_coord_msg.z = Z_world
        self.world_publisher.publish(world_coord_msg)
        self.get_logger().info(f"Published world coordinates: X={X:.2f} cm, Y={Y:.2f} cm, Z={Z_world:.2f} cm")

def main(args=None):
    rclpy.init(args=args)
    combined_node = cam_coord_transform()
    try:
        rclpy.spin(combined_node)
    except KeyboardInterrupt:
        combined_node.get_logger().info("Shutting down Combined Transform Node.")
    finally:
        combined_node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
