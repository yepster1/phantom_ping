import cv2
import time
import threading
import networkManager as nm

queue = []

#thread for displaying the videos in the queue
class video_shower(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)

  def run(self):
    print("video shower started")
    while True:
        queue = nm.get_videos()
        while len(queue) > 0:
            queue = nm.get_videos()
            print(len(queue))
            for video in queue:
                display_video(video)
        time.sleep(5)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

def display_video(frames):
    for frame in frames:
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        cv2.waitKey(50)

if __name__ == "__main__":
    worker = video_shower()
    worker.start()
    nm.displayer_recieve()
