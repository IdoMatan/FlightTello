from TelloControl.tello import Tello
import cv2
import numpy as np


def fly():
    tello = Tello(host='192.168.10.1', port=8889, client_socket=None, enable_exceptions=True, retry_count=3)
    tello.connect()
    tello.streamon()
    tello.takeoff()
    while True:
        frame_read = tello.get_frame_read()
        frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        frame = np.flipud(frame)

        tello.rotate_counter_clockwise(45)

        tello.move_left(1)

    tello.land()
    tello.end()


if __name__ == '__main__':
    fly()