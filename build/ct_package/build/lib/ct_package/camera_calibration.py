import cv2
import numpy as np
import glob
import rclpy
from rclpy.node import Node


class Calibration(Node):
    
    def __init__(self):
        super().__init__('calibration_node')
        
        self.chessboard_size = (7, 7)  # 체스보드의 내부 코너 개수 (행, 열)
        self.square_size = 1.0  # 각 사각형의 크기 (단위는 실제 크기, 예: mm, cm 등)
        
        # 체스보드의 3D 점 (세계 좌표계의 3D 점)
        self.object_points_3d = np.zeros((self.chessboard_size[0] * self.chessboard_size[1], 3), np.float32)
        self.object_points_3d[:, :2] = np.mgrid[0:self.chessboard_size[0], 0:self.chessboard_size[1]].T.reshape(-1, 2)
        self.object_points_3d *= self.square_size
        
        # 모든 이미지에서 2D 이미지 포인트와 3D 객체 포인트를 저장할 배열
        self.object_points = []  # 3D 점 (세계 좌표계)
        self.image_points = []  # 2D 점 (이미지 좌표계)
        
        # 이미지 파일 경로 패턴
        self.image_path_pattern = '/home/pi/ControlTower/src/ct_package/ct_package/images/*.jpg'
        self.images = self.load_images(self.image_path_pattern)
        
        self.image_shape = None  # 이미지 크기를 저장하기 위한 변수
        
        # 코너 검출의 정확도를 높이기 위한 반복 알고리즘의 종료 기준
        self.criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    
    def load_images(self, path_pattern):
        """
        주어진 경로 패턴에 맞는 모든 이미지 파일을 읽어 리스트로 반환합니다.
        """
        image_files = glob.glob(path_pattern)
        if not image_files:
            self.get_logger().error(f"No images found with the pattern: {path_pattern}")
        return image_files
    
    def read_img(self):
        """
        이미지 파일을 읽어 체스보드 코너를 검출합니다.
        """
        for image_file in self.images:
            image = cv2.imread(image_file)
            if image is None:
                self.get_logger().warn(f"Failed to read image: {image_file}")
                continue
            
            if self.image_shape is None:
                self.image_shape = image.shape[:2][::-1]  # 첫 번째 이미지의 크기를 저장
            
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            self.find_corner(gray)
    
    def find_corner(self, gray):
        """
        체스보드에서 코너를 검출하고, 검출된 코너를 이미지에 표시합니다.
        """
        ret, corners = cv2.findChessboardCorners(gray, self.chessboard_size, None)

        if ret:
            self.object_points.append(self.object_points_3d)

            # 서브픽셀 정확도로 코너를 찾기
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), self.criteria)
            self.image_points.append(corners2)
            
            # 코너 그리기 및 결과 보기
            cv2.drawChessboardCorners(gray, self.chessboard_size, corners2, ret)
            cv2.imshow('Corners', gray)
            cv2.waitKey(500)
        else:
            self.get_logger().warn("Chessboard corners not found in the image.")

        cv2.destroyAllWindows()

    def calibration(self):
        """
        카메라 보정을 수행하고 결과를 출력합니다.
        """
        if not self.object_points or not self.image_points:
            self.get_logger().error("Not enough valid images with detected corners to perform calibration.")
            return None, None, None, None, None
        
        # 카메라 보정 수행
        ret, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(self.object_points, self.image_points, self.image_shape, None, None)
        
        # 카메라 보정 결과 출력
        print("Camera Matrix:\n", camera_matrix)
        print("Distortion Coefficients:\n", dist_coeffs)
        print("Rotation Vectors:\n", rvecs)
        print("Translation Vectors:\n", tvecs)
        
        return ret, camera_matrix, dist_coeffs, rvecs, tvecs

    # 이미지에서 카메라 좌표를 월드 좌표로 변환하는 함수
    def camera_to_world(self, image_point, rvec, tvec, camera_matrix, dist_coeffs):
        """
        이미지 좌표를 카메라 좌표로 변환한 후, 이를 월드 좌표로 변환합니다.
        """
        # 이미지 좌표를 undistort하여 실제 카메라 좌표로 변환
        image_point_undistorted = cv2.undistortPoints(np.array([image_point], dtype=np.float32), camera_matrix, dist_coeffs)
        
        # 역회전 벡터 계산
        rmat, _ = cv2.Rodrigues(rvec)
        rmat_inv = np.linalg.inv(rmat)
        
        # 역변환하여 월드 좌표 계산
        world_point = np.dot(rmat_inv, (image_point_undistorted[0][0] - tvec).reshape(-1, 1))
        return world_point


def main(args=None):
    rclpy.init(args=args)
    calibrator = Calibration()
    calibrator.read_img()  # 이미지 읽기 및 코너 검출 수행
    calibrator.calibration()  # 카메라 보정 수행

    try:
        rclpy.spin(calibrator)
    except KeyboardInterrupt:
        pass
    finally:
        cv2.destroyAllWindows()
        calibrator.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
