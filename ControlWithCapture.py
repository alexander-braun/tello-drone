import KeypressModule as kp
from djitellopy import tello
from time import sleep
import cv2
import KeyboardControl as kc

me = tello.Tello()
me.connect()
me.streamon()

while True:
    # img
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)

    #control
    vals = kc.getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.1)
    