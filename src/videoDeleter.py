import config as c
import os
import time

def delete_files():
    deletefrom = c.get_delete_from(time.time())
    print(deletefrom)
    while(True):
        try:
            os.remove(c.get_raw_directory() + str(deletefrom) + ".avi")
            deletefrom -= 1
        except:
            try:
                deletefrom -= 1
                os.remove(c.get_raw_directory() + str(deletefrom) + ".avi")
            except:
                print(c.get_raw_directory() + str(deletefrom) + ".avi")
                time.sleep(10)
                deletefrom = c.get_delete_from(time.time())


if __name__ == "__main__" :
    delete_files()
