import cv2
import numpy as np
import glob
from rclpy.node import Node
import rclpy
from std_msgs.msg import Float32MultiArray

# 캘리브레이션 수행 코드
class Calibration(Node):
    def __init__(self):
        super().__init__('calibration_node')
        self.chessboard_size = (7, 7)  # 체스보드의 내부 코너 개수 (행, 열)
        self.square_size = 3  # 각 사각형의 크기 (단위는 실제 크기, 예: mm, cm 등)
        
        # 체스보드의 3D 점 (세계 좌표계의 3D 점)
        self.object_points_3d = np.zeros((self.chessboard_size[0] * self.chessboard_size[1], 3), np.float32)
        self.object_points_3d[:, :2] = np.mgrid[0:self.chessboard_size[0], 0:self.chessboard_size[1]].T.reshape(-1, 2)
        self.object_points_3d *= self.square_size
        
        # 모든 이미지에서 2D 이미지 포인트와 3D 객체 포인트를 저장할 배열
        self.object_points = []  # 3D 점 (세계 좌표계)
        self.image_points = []  # 2D 점 (이미지 좌표계)
        
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
        
        # 파라미터를 발행하기 위한 ROS publisher 생성
        self.param_publisher = self.create_publisher(Float32MultiArray, 'camera_parameters', 10)
        
        # 카메라 보정 수행
        self.read_images_and_find_corners()
        self.calibrate_camera()
        
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
                self.image_shape = image.shape[:2][::-1]  # 첫 번째 이미지의 크기를 저장
            
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            self.find_corners(gray)
    
    def find_corners(self, gray):
        """
        체스보드에서 코너를 검출하고, 검출된 코너를 저장합니다.
        """
        ret, corners = cv2.findChessboardCorners(gray, self.chessboard_size, None)

        if ret:
            self.object_points.append(self.object_points_3d)

            # 서브픽셀 정확도로 코너를 찾기
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), self.criteria)
            self.image_points.append(corners2)
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
            # 파라미터 발행
            self.publish_parameters()
        else:
            self.get_logger().error("Camera calibration failed.")
    
    def publish_parameters(self):
        """
        보정된 파라미터를 발행합니다.
        """
        # camera_matrix는 3x3
        camera_matrix_flat = self.camera_matrix.flatten().tolist()
        
        # dist_coeffs는 (1,5) 혹은 (1, k)
        dist_coeffs_flat = self.dist_coeffs.flatten().tolist()
        
        # rvecs와 tvecs는 여러 이미지에 대한 리스트이므로, 여기서는 첫 번째 값을 사용합니다.
        rvec = self.rvecs[0].flatten()
        tvec = self.tvecs[0].flatten()
        
        # 메시지 생성
        param_msg = Float32MultiArray()
        param_msg.data = camera_matrix_flat + dist_coeffs_flat + rvec.tolist() + tvec.tolist()
        
        # 발행
        self.param_publisher.publish(param_msg)
        self.get_logger().info(f"Published camera parameters: camera_matrix={self.camera_matrix.tolist()}, dist_coeffs={self.dist_coeffs.tolist()}, rvec={rvec.tolist()}, tvec={tvec.tolist()}")
    
def main(args=None):
    rclpy.init(args=args)
    calibration_node = Calibration()
    rclpy.spin(calibration_node)
    calibration_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
