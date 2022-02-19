import KeypressModule as kp
from djitellopy import tello
from time import sleep

kp.init()
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

while True:
    vals = getKeyboardInput()

    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.1)
    