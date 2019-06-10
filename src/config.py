def get_back_time():
    return 2

def get_forward_time():
    return 2

def get_raw_directory():
    return "../data/"

def get_start(time):
    return round(time/10) -  get_back_time()

def get_end(time):
    return round(time/10) +  get_forward_time()
