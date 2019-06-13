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
    e = 0
    print(str(start))
    print(str(end))
    while(start <= end):
        result = add_next_video(frames, start)
        if result == [] :
            if e == 3:
                frames = frames
            else:
                end += 1
                start += 1
                e += 1
                continue
        print(start)
        start += 1
    return frames

def add_next_video(frames, counterTime):
    videoDirectory = c.get_raw_directory() + str(counterTime) + ".avi"
    print("reading video at " + videoDirectory)
    cap = cv2.VideoCapture(videoDirectory)
    if (cap.isOpened() == False):
        print("Error opening video stream or file " + str(videoDirectory))
        return []
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frames.append(frame)
        else:
            break
    cap.release()
    return frames

def read_video(videoName):
    videoDirectory = c.get_raw_directory() + str(videoName) + ".avi"
    print("reading video at " + videoDirectory)
    cap = cv2.VideoCapture(videoDirectory)
    return cap

if __name__ == "__main__" :
    # print(list_all_files(c.config.get_raw_directory()))
    print(len(combine_videos_between_timestamps(c.get_start(156015544*10), c.get_end(156015544*10))))
