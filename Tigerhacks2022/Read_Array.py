<<<<<<< HEAD
from djitellopy import tello
from time import sleep
#yes


#speed variables:
global slow
slow_speed = 25
global med
med_speed = 50
global fast
fast_speed = 100

 

def run_drone_que(array):
    # array=[]
    # array= ['Fast', 'Turn Left', '360']
    # array= ['Fast', 'Forward', '300', 'Med', 'Backwards', '300', 'Slow', 'Forward', '300']
    print(len(array))
    if len(array) !=0:
        me = tello.Tello()
        me.connect()
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



=======
from djitellopy import tello
from time import sleep
#yes


#speed variables:
global slow
slow_speed = 25
global med
med_speed = 50
global fast
fast_speed = 100

 

def run_drone_que(array):
    # array=[]
    # array= ['Fast', 'Turn Left', '360']
    # array= ['Fast', 'Forward', '300', 'Med', 'Backwards', '300', 'Slow', 'Forward', '300']
    print(len(array))
    if len(array) !=0:
        me = tello.Tello()
        me.connect()
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



>>>>>>> c00e913585e6c2d10a07d58ffcfda1b6d57a750d
# run_drone_que()