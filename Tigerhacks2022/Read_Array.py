from djitellopy import tello
from time import sleep
import Main_with_better_layout as Main
#yes


#speed variables:
global slow
slow_speed = 25
global med
med_speed = 50
global fast
fast_speed = 100



def run_drone_que():
    save_array=Main.command_que
    array = save_array
    print(len(array))
    if len(array) !=0:
        me = tello.Tello()
        me.connect()
        print(me.get_battery())
        me.takeoff()
        while len(array) != 0:

            print(array)
            print(len(array))
            speed = array.pop(0)
            movement = array.pop(0)
            distance = array.pop(0)
            distance = int(distance)

            print(speed)
            print(movement)
            print(speed)
            #Speed if statements
            if speed == 'Slow':
                me.set_speed(slow_speed)
            if speed == 'Med':
                me.set_speed(med_speed)
            if speed == 'Fast':
                me.set_speed(fast_speed)
            sleep(2)
            #Movement if statements
            if movement == 'Forward':
                me.move_forward(distance)
            elif movement == 'Backwards':
                me.move_back(distance)
            elif movement == 'Left':
                me.move_left(distance)
            elif movement == 'Right':
                me.move_right(distance)
            elif movement == 'Turn Left':
                me.rotate_counter_clockwise(distance)
            elif movement == 'Turn Right':
                me.rotate_clockwise(distance)
                
        me.land()