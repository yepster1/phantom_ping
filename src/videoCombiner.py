import config as c
import time as time
import os
import cv2
import numpy as np

def list_all_files(path):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.avi' in file:
                files.append(file)

    return files

def combine_videos_at_timestamps(start, end):
    return video

#combines the frames of 2 vidoes
def combine_two_videos(first, second):

def read_next_video(counterTime):
    counterTime += 10
    return False

def read_video(videoName):
    cap = cv2.VideoCapture(str(videoName))
    return cap

if __name__ == "__main__" :
    # print(list_all_files(c.config.get_raw_directory()))
    combine_two_videos(c.config.get_raw_directory() + "1560150754.8829465.avi", c.config.get_raw_directory() + "1560150765.1732647.avi")
