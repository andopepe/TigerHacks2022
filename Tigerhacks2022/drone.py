# f = open("\Users\coolc\Desktop\College\Mizzou\Clubs\Robotics\Drone Workshop\drone.py")
from time import sleep
from djitellopy import tello


me = tello.Tello()
me.connect()
print(me.get_batter())

me.takeoff()
me.send_rc_control(0,50,0,0)
sleep(2)
me.send_rc_control(0,-50,0,0)
sleep(2)
me.send_rc_control(0,0,0,0)


me.land()
# me.move_forward(30)

# tello=Tello()
# tello.connect()
# tello.takeoff()
# tello.land()