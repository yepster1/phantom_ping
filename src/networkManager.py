import socket                   # Import socket module
import config as c
import pickle as p
import videoWriter as vw
import time

queue = []
def get_videos():
    return queue

def pi_send(video):
    s = socket.socket()             # Create a socket object
    host = c.get_displayer_ip()
    port = 50000

    print('sendingVideo')
    s.connect((host, port))
    pickled = p.dumps(video)
    len(pickled)
    s.send(pickled)

    s.close()
    print('sent video')

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
        data = []
        while(True):
            packet = conn.recv(4096)
            if not packet: break
            data.append(packet)
        data_arr = p.loads(b"".join(data))
        print("video recieved")
        queue.append(data_arr)
        if(len(queue) > c.get_max_queue_size():
            del queue[-1]
        vw.write_to_file(data_arr, c.get_finished_directory()+str(time.time()) + ".avi", 640, 480, 20)
        conn.close()
