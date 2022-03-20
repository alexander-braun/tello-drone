import KeypressModule as kp
from djitellopy import tello
import time
import cv2

me = tello.Tello()
me.connect()
print(me.get_battery())

def getKeyboardInput(img = None):
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    
    if kp.getK("a"): lr = -speed
    elif kp.getK("d"): lr = speed
    
    if kp.getK("UP"): ud = speed
    elif kp.getK("DOWN"): ud = -speed
    
    if kp.getK("w"): fb = speed
    elif kp.getK("s"): fb = -speed
    
    if kp.getK("e"): yv = speed
    elif kp.getK("q"): yv = -speed
    
    if kp.getK('l'): me.land()
    if kp.getK('t'): me.takeoff()

    if kp.getK('p') and img: 
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
        time.sleep(0.5)
    
    return [lr, fb, ud, yv]