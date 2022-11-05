# flight time is around thirteen mins
#max speed is 8 m/s
#range 300-350 ft
from glob import glob
from djitellopy import tello
import KeyPressModule as kp
import time
import cv2
import numpy as np



### Paras ###
fSpeed=117/10 #fwd speed cm/s
aSpeed=360/10 #Angle speed degrees/s
interval =0.25

dInterval = fspeed*interval
aInterval = aspeed*interval
#############

kp.init()
me= tello.Tello()
me.connect()
print(me.get_battery())

global img
me.streamon()



def getKeyboardInput():
    global speed
    lr,fb, ud, yv = 0,0,0,0
    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed
    
    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

    
    if kp.getKey("a"): yv = -speed
    elif kp.getKey("d"): yv = speed

    if kp.getKey("q"): me.land(); time.sleep(3)
    if kp.getKey("e"): me.takeoff()

    if kp.getKey("i"):
        if speed<500:  
            speed += 1   
        time.sleep(.1)
    elif kp.getKey("k"):
        if speed>25: 
            speed -= 1
        else
            print("Drone will not move with speed < 25")
        time.sleep(.1)


    if kp.getKey("z"): 
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
        time.sleep(.1)


    return [lr, fb, ud, yv]

def drawPoints():
    cv2.circle(map, (300,500),20,(0,0,255),cv2.FILLED)

while True:
    # me.get_lowest_temperature()
    vals = getKeyboardInput()
    me.send_rc_control(vals[0],vals[1],vals[2],vals[3])
    print(speed)


    map= np.zeros((1000, 1000, 3), np.uint8)

    drawPoints()

    img = me.get_frame_read().frame
    img = cv2.resize(img,(360,240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    