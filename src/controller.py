import videoCombiner as vc
import videoWriter as vw
import config as c
import networkManager as nm
import cv2
import time
import threading

queue = []

def recieve_video(video):
    vw.write_to_file(video, c.get_finished_directory() + str(round(currentTime/10)) + ".avi", 0, 0,0)
    queue.append(combinedVideo)

def recieve_ping():
    currentTime = time.time()
    start = c.get_start(currentTime)
    end = c.get_end(currentTime)
    time.sleep(c.get_forward_time() * 10)
    combinedVideo = vc.combine_videos_between_timestamps(start, end)
    send_video(combinedVideo)

def send_video(video):
    print("phsodo Sending video")
    nm.pi_send(video)
    #send video to other pc

if __name__ == "__main__" :
    recieve_ping()
    time.sleep(30)
    while(True):
        recieve_ping()
        time.sleep(20)
