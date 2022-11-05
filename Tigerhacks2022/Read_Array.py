from djitellopy import tello
from time import sleep
import tinktrGUI.py
me = tello.tello()
me.connect()

#speed variables:
global Slow
Slow = 25
global Med
Med = 50
global Fast
Fast = 100


array = tinktrGUI.command_que

while len(array) != 0:

    speed = array.pop()
    movement = array.pop()
    distance = array.pop()

    #Speed if statements
    if speed == 'Slow':
        me.set_speed(Slow)
    if speed == 'Med':
        me.set_speed(Med)
    if speed == 'Fast':
        me.set_speed(Fast)

    #Movement if statements
    if movement == 'Forward':
        me.move_forward(distance)
    elif movement == 'Backwards':
        me.move_backward(distance)
    elif movement == 'Left':
        me.move_left(distance)
    elif movement == 'Right':
        me.move_right(distance)
    elif movement == 'Turn Left':
        me.rotate_counter_clockwise(distance)
    elif movement == 'Turn Right':
        me.rotate_clockwise(distance)
