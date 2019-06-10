import cv2
import time
import config as c

def main():
    frames = record()
    cv2.waitKey()

def record():
    # records 5 second snippits of video
    timeout = time.time() + 5
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    frames = []
    while ret:
        ret, frame = cap.read()
        frames.append(frame)
        cv2.imshow('frame',frame)
        if time.time() > timeout:
            write_to_file(frames, c.config.get_raw_directory() + str(round(time.time()/10)) + ".avi", int(cap.get(3)), int(cap.get(4)), int(cap.get(5)))
            timeout = time.time() + 10
            frames = []
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def write_to_file(frames, output, vw, vh, vfps):
    if not str.endswith(output, ".avi"):
        print("background.py: error: can only output AVI video files (*.avi extension)")
        exit(1)

    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    vout = cv2.VideoWriter(output, fourcc, vfps, (vw, vh))

    if not vout.isOpened():
        print("background.py: error: couldn't initialise output codec")
        exit(1)
    for frame in frames:
        vout.write(frame)
    vout.release()

if __name__ == "__main__":
    main()
