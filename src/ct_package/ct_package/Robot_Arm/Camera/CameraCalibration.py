import cv2
import numpy as np
import glob
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class Calibration(Node):
    
    def __init__(self):
        super().__init__('calibration_node')
        
        self.chessboard_size = (9, 6)  # ü�������� ���� �ڳ� ���� (��, ��)
        self.square_size = 1.0  # �� �簢���� ũ�� (������ ���� ũ��, ��: mm, cm ��)
        
        # ü�������� 3D �� (���� ��ǥ���� 3D ��)
        self.object_points_3d = np.zeros((self.chessboard_size[0] * self.chessboard_size[1], 3), np.float32)
        self.object_points_3d[:, :2] = np.mgrid[0:self.chessboard_size[0], 0:self.chessboard_size[1]].T.reshape(-1, 2)
        self.object_points_3d *= self.square_size
        
        # ��� �̹������� 2D �̹��� ����Ʈ�� 3D ��ü ����Ʈ�� ������ �迭
        self.object_points = []  # 3D �� (���� ��ǥ��)
        self.image_points = []  # 2D �� (�̹��� ��ǥ��)
        self.images = glob.glob('/home/pi/MasterPi/CameraCalibration/calibration_images*.jpg')
        self.image_shape = None  # �̹��� ũ�⸦ �����ϱ� ���� ����
        
        # �ڳ� ������ ��Ȯ���� ���̱� ���� �ݺ� �˰����� ���� ����
        self.criteria = (cv2.TermCriteria_EPS + cv2.TermCriteria_MAX_ITER, 30, 0.001)
    
    def read_img(self):
        # �̹��� ���� �б� �� ó��
        for image_file in self.images:
            image = cv2.imread(image_file)
            if self.image_shape is None:
                self.image_shape = image.shape[:2][::-1]  # ù ��° �̹����� ũ�⸦ ����
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            self.find_corner(gray)
    
    def find_corner(self, gray):
        # ü������ �ڳ� ã��
        ret, corners = cv2.findChessboardCorners(gray, self.chessboard_size, None)

        if ret:
            self.object_points.append(self.object_points_3d)

            # �����ȼ� ��Ȯ���� �ڳʸ� ã��
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), self.criteria)
            self.image_points.append(corners2)
            
            # �ڳ� �׸��� �� ��� ����
            cv2.drawChessboardCorners(gray, self.chessboard_size, corners2, ret)
            cv2.imshow('Corners', gray)
            cv2.waitKey(500)

        cv2.destroyAllWindows()

    def calibration(self):
        # ī�޶� ���� ����
        ret, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(self.object_points, self.image_points, self.image_shape, None, None)
        
        # ī�޶� ���� ��� ���
        print("Camera Matrix:\n", camera_matrix)
        print("Distortion Coefficients:\n", dist_coeffs)
        print("Rotation Vectors:\n", rvecs)
        print("Translation Vectors:\n", tvecs)
        
        return ret, camera_matrix, dist_coeffs, rvecs, tvecs

    # �̹������� ī�޶� ��ǥ�� ���� ��ǥ�� ��ȯ�ϴ� �Լ�
    def camera_to_world(self, image_point, rvec, tvec, camera_matrix, dist_coeffs):
        # �̹��� ��ǥ�� undistort�Ͽ� ���� ī�޶� ��ǥ�� ��ȯ
        image_point_undistorted = cv2.undistortPoints(np.array([image_point], dtype=np.float32), camera_matrix, dist_coeffs)
        
        # ��ȸ�� ���� ���
        rmat, _ = cv2.Rodrigues(rvec)
        rmat_inv = np.linalg.inv(rmat)
        
        # ����ȯ�Ͽ� ���� ��ǥ ���
        world_point = np.dot(rmat_inv, (image_point_undistorted[0][0] - tvec).reshape(-1, 1))
        return world_point


def main(args=None):
    rclpy.init(args=args)
    calibrator = Calibration()
    calibrator.read_img()  # �̹��� �б� �� �ڳ� ���� ����
    calibrator.calibration()  # ī�޶� ���� ����

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


