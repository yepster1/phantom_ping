import videoCombiner as vc
import videoWriter as vw
import config as c
import networkManager as nm
import cv2
import time
import threading
import keyboard

queue = []

def recieve_video(video):
    vw.write_to_file(video, c.get_finished_directory() + str(round(currentTime/10)) + ".avi", 0, 0,0)
    queue.append(combinedVideo)

def send_ping():
    currentTime = time.time()
    start = c.get_start(currentTime)
    end = c.get_end(currentTime)
    nm.pi_send_ping()

if __name__ == "__main__" :
    time.sleep(5)
    print("pinging")
    send_ping()
