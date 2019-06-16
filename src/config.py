def get_back_time():
    return 1

def get_forward_time():
    return 2

def get_raw_directory():
    return "../data/"

def get_finished_directory():
    return "../finishedVideos/"

def get_start(time):
    return round(time/10) -  get_back_time()

def get_end(time):
    return round(time/10) +  get_forward_time()

def get_delete_from(time):
    return round(time/10) -  10

#set these to correct ips
def get_displayer_ip():
    return "192.168.0.119"

#set these to correct ips
def get_pi_ip():
    return "127.0.0.1"

def get_max_queue_size():
    return 5

def get_video_width():
    return 640

def get_video_height():
    return 480

def get_video_frames():
    return 20

def get_camara_input_location():
    return 0

#color in RGB
def get_text_color():
    return (255, 255, 255)

def get_text_scale():
    return 1

def black_and_white():
    return True
