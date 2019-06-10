import videoCombiner as vc
import config as c
import cv2
import time
import threading

queue = []

#thread for showing the queue
class video_shower(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)

  def run(self):
    print("video shower started")
    while True:
        print(queue)
        while len(queue) > 0:
            for video in queue:
                display_video(video)
        time.sleep(5)

def recieve_ping():
    print("ping recieved")
    currentTime = time.time()
    start = c.get_start(currentTime)
    end = c.get_end(currentTime)
    time.sleep(c.get_forward_time() * 10)
    queue.append(vc.combine_videos_between_timestamps(start, end))

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
    recieve_ping()
