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
    cv2.namedWindow("phantom", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Phantom",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    print("video shower started")
    while True:
        queue = nm.get_videos()
        while len(queue) > 0:
            queue = nm.get_videos()
            for video in queue[::-1]:
                display_video(video)

        time.sleep(5)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

def display_video(frames):
    for frame in frames:
        resize = cv2.resize(frame, (1280,960), interpolation=cv2.INTER_LINEAR)
        cv2.imshow('phantom', resize)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        cv2.waitKey(30)

if __name__ == "__main__":
    worker = video_shower()
    worker.start()
    nm.displayer_recieve()
