__author__ = 'Yijun Pan'


import cv2
import numpy as np



class VideoRGBD:
    filenames = []
    dirpath = []
    color_frame = []
    depth_frame = []
    nframe = 0
    camera_matrix_color = []
    camera_matrix_depth = []

    def __init__(self):
        pass

    def __init__(self, input_list):
        self.read_list(input_list)

    def __init__(self, input_list, cam_mat_file):
        self.read_list(input_list)
        self.read_camera_matrix(cam_mat_file)

    def read_list(self, input_list):
        with open(input_list, 'r') as f:
            # TODO: add input_list to file names
            idx = input_list.rfind("/")
            self.dirpath = input_list[:idx+1]
            self.filenames = f.readlines()

    def read_camera_matrix(self, cam_mat_file):
        with cv2.FileStorage(cam_mat_file) as fs:
            self.camera_matrix_depth = fs["camera_matrix_depth"]
            self.camera_matrix_color = fs["camera_matrix_color"]

    def load_frame(self):
        for f in self.filenames:
            f_c = self.dirpath + f.rstrip() + '_color.jpg'
            f_d = self.dirpath + f.rstrip() + '_depth.png'
            # print f_c
            # print f_d
            # Load a pair of color and depth image
            img_c = cv2.imread(f_c, cv2.CV_LOAD_IMAGE_COLOR)
            img_d = cv2.imread(f_d, cv2.CV_LOAD_IMAGE_GRAYSCALE)

            self.color_frame.append(img_c)
            self.depth_frame.append(img_d)

            self.nframe += 1
            print "Successfully load frame %s" % f




if __name__ == '__main__':
    input_list = '../data/frames.txt'
    video = VideoRGBD(input_list)
    video.load_frame()
    cv2.imshow('image', video.color_frame[0])
    cv2.waitKey(0)
    cv2.destroyAllWindows()


