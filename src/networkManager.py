import socket                   # Import socket module
import config as c
import struct
import pickle as p
import videoWriter as vw
import time
import videoCombiner as vc
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

def displayer_recieve():
    s = socket.socket()             # Create a socket object
    host = c.get_displayer_ip()
    port = 50000
    s.bind((host, port))
    s.listen(5)

    print('Server listening....')

    while True:
        conn, addr = s.accept()     # Establish connection with client.
        print('Got connection from', addr)
        packet = conn.recv(4096)
        startTime = c.get_start(time.time())
        endTime = c.get_end(time.time())
        time.sleep((c.get_forward_time()+1) * 10)
        video = vc.combine_videos_between_timestamps(startTime, endTime)
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
