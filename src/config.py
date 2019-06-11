def get_back_time():
    return 2

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
    return "127.0.0.1"

#set these to correct ips
def get_pi_ip():
    return "127.0.0.1"

def get_max_queue_size():
    return 5
