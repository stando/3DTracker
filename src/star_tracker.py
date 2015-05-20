__author__ = 'stando'

import scipy as sp
import numpy as np
import rgbd_video

'''
Main class for the RGBD tracking algorithm from Carl Yuheng Ren.
Star3D: Simultaneous Tracking and Reconstruction of 3D Objects Using RGB-D Data

'''
class StarTracker:

    # A reference to the video frames
    __sequence = None
    __curr_frame = 0

    def __init__(self):
        pass

    def __init__(self, vid):
        """

        :param vid: rgbd_video.VideoRGBD
        :return: void
        """
        self.set_sequence(vid)

    def set_sequence(self, vid):
        """

        :param vid: rgbd_video.VideoRGBD
        :return: void
        """
        self.__sequence = vid
        self.__curr_frame = 0

    def is_initialized(self):

        if self.__sequence is not rgbd_video.VideoRGBD:
            return False
        elif self.__sequence.nframe < 1:
            return False
        else:
            return True

    def current_frame(self):
        return self.__curr_frame








