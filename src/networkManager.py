import socket                   # Import socket module
import config as c
import struct
import pickle as p
import videoWriter as vw
import time
import videoCombiner as vc
import cv2

queue = []

def get_videos():
    return queue

def pi_send_ping():
    print('pinging')
    s = socket.socket()             # Create a socket object
    host = c.get_displayer_ip()
    port = 50000
    s.connect((host, port))
    s.send(bytearray(struct.pack("f",time.time())))
    s.close()
    print('ping sent')

def add_empty_at_end(video):
    frame = video[0]
    frame2 = video[1]
    for x in range(len(frame)):
        for y in range(len(frame[x])):
            frame2[x][y] = [50,200,0]
    for _ in range(5):
        video.append(frame2)
    return video

def __draw_label(img, text, pos, bg_color):
    font_face = cv2.FONT_HERSHEY_SIMPLEX
    scale = 1
    color = (255, 255, 255)
    thickness = cv2.FILLED
    margin = 2

    txt_size = cv2.getTextSize(text, font_face, scale, thickness)

    end_x = pos[0] + txt_size[0][0] + margin
    end_y = pos[1] - txt_size[0][1] - margin

    cv2.putText(img, text, pos, font_face, scale, color, 1, cv2.LINE_AA)

def add_top_text(time, counter, video):
    for x in range(len(video)):
        __draw_label(video[x], str(time), (0,25), (0,0,0))
        __draw_label(video[x], str(counter), (600,0), (0,0,0))
    return video

def add_ping_text(video):
    start = len(video)//2
    for x in range(start,len(video),1):
        __draw_label(video[x], str("you got pinged"), (20,400), (0,0,0))
    return video

def displayer_recieve():
    s = socket.socket()             # Create a socket object
    host = c.get_displayer_ip()
    port = 50000
    s.bind((host, port))
    s.listen(5)

    print('Server listening....')
    counter = 0
    while True:
        conn, addr = s.accept()     # Establish connection with client.
        print('Got connection from', addr)
        packet = conn.recv(4096)
        currentTime = time.time()
        startTime = c.get_start(time.time())
        endTime = c.get_end(time.time())
        time.sleep((c.get_forward_time()+1) * 10)
        video = vc.combine_videos_between_timestamps(startTime, endTime)
        video = add_top_text(currentTime, counter, video)
        video = add_ping_text(video)
        video = add_empty_at_end(video)
        counter+=1
        queue.insert(0, video)
        print("queue size: " + str(len(queue)))
        if(len(queue) > c.get_max_queue_size()) :
            print("queue big deleting end")
            del queue[-1]
        vw.write_to_file(
            video,
            c.get_finished_directory()+str(time.time()) + ".avi",
            c.get_video_width(),
            c.get_video_height(),
            c.get_video_frames())
        print("ping recieved recieved")
        conn.close()
