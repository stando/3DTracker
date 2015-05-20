import argparse
import os
import rgbd_video as video

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', nargs='?', default='../data/input_sequence.txt',
                        help='The list containing each frame of the video sequence.')

    parser.add_argument('-c', nargs='?', default='../data/camera_matrix.yml',
                        help='YML file containing depth camera matrix and color camera matrix.')

    args = parser.parse_args()
    video_rgbd = video.VideoRGBD(args.i)


if __name__ == "__main__":
    main()
