import cv2
import random
import config as c
import time as t

def distort_video(video, counter):
    if(c.add_empty_at_end()):
        video = add_empty_at_end()

    if(c.black_and_white()):
        video = make_video_black_and_white()
    video = add_top_text(t.time(), counter, video)
    video = add_ping_text(video)
    return video

def add_empty_at_end(video):
    frame = video[0]
    frame2 = video[1]
    for x in range(len(frame)):
        for y in range(len(frame[x])):
            frame2[x][y] = [50,200,0]
    for _ in range(5):
        video.append(frame2)
    return video

def __draw_label(img, text, pos):
    font_face = cv2.FONT_HERSHEY_SIMPLEX
    scale = c.get_text_scale()
    color = c.get_text_color()
    thickness = cv2.FILLED
    margin = 2

    txt_size = cv2.getTextSize(text, font_face, scale, thickness)

    end_x = pos[0] + txt_size[0][0] + margin
    end_y = pos[1] - txt_size[0][1] - margin

    cv2.putText(img, text, pos, font_face, scale, color, 1, cv2.LINE_AA)

def add_top_text(time, counter, video):
    for x in range(len(video)):
        __draw_label(video[x], str(time), (0,25))
        __draw_label(video[x], str(counter), (600,25))
    return video

def add_ping_text(video):
    start = len(video)//2
    pingText =str(random.choice(text))
    for x in range(start,len(video),1):
        __draw_label(video[x], pingText, (20,400))
    return video

def make_video_black_and_white(video):
    frames = []
    for frame in video:
        frames.append(make_frame_black_and_white(frame))
    return frames

def make_frame_black_and_white(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
