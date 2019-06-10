import videoCombiner as vc
import config as config

queue = []

def recieve_ping():
    currentTime = time.time()
    startTime = time.time() - config.get_back_time()
    endTime = time.time() + config.get_forward_time()
    queue.append(vc.combine_videos_at_timestamps(startTime, endTime))

def video_shower():
