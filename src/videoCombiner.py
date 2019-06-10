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

def combine_videos_between_timestamps(start, end):
    frames = []
    while(start < end):
        video = read_next_video(start)
        frames = add_next_video(frames, video)
        print(start)
        start += 1
    return frames

def add_next_video(frames, cap):
    if (cap.isOpened()== False):
        print("Error opening video stream or file " + str(cap))
    while(cap.isOpened()):

        ret, frame = cap.read()
        if ret == True:
            frames.append(frame)
        else:
            break
    cap.release()
    return frames

#combines the frames of 2 vidoes
def combine_two_videos(first, second):
    cap = read_video(first)
    cap1 = read_video(second)
    if (cap.isOpened()== False):
        print("Error opening video stream or file " + str(first))

    if (cap1.isOpened()== False):
        print("Error opening video stream or file " + str(second))

    frames = []
    while(cap.isOpened()):

        ret, frame = cap.read()
        if ret == True:
            frames.append(frame)
        else:
            break
    while (cap1.isOpened()):
        ret, frame = cap1.read()
        if ret == True:
            frames.append(frame)
        else:
            break

    cap.release()
    cap1.release()

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return frames

def read_next_video(counterTime):
    return read_video(counterTime)

def read_video(videoName):
    videoDirectory = c.get_raw_directory() + str(videoName) + ".avi"
    print("reading video at " + videoDirectory)
    cap = cv2.VideoCapture(videoDirectory)
    return cap

if __name__ == "__main__" :
    # print(list_all_files(c.config.get_raw_directory()))
    print(len(combine_videos_between_timestamps(c.get_start(156015544*10), c.get_end(156015544*10))))
