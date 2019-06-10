import videoCombiner as vc
import videoWriter as vw
import config as c
import cv2
import time
import threading

queue = []

#thread for displaying the videos in the queue
class video_shower(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)

  def run(self):
    print("video shower started")
    while True:
        while len(queue) > 0:
            for video in queue:
                display_video(video)
        time.sleep(5)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

def recieve_ping():
    print("ping recieved")
    currentTime = time.time()
    start = c.get_start(currentTime)
    end = c.get_end(currentTime)
    time.sleep(c.get_forward_time() * 10)
    combinedVideo = vc.combine_videos_between_timestamps(start, end)
    vw.write_to_file(combinedVideo, c.get_finished_directory() + str(round(currentTime/10)) + ".avi", 0, 0,0)
    queue.append(combinedVideo)

def display_video(frames):
    for frame in frames:
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        cv2.waitKey(50)

if __name__ == "__main__" :
    worker = video_shower()
    worker.start()
    recieve_ping()
    time.sleep(30)
    while(True):
        recieve_ping()
        time.sleep(20)
