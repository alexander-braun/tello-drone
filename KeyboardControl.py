import KeypressModule as kp
from djitellopy import tello
from time import sleep


me = tello.Tello()
me.connect()
print(me.get_battery())

def getKeyboardInput():
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
    
    return [lr, fb, ud, yv]