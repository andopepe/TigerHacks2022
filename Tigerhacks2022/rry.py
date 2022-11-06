from djitellopy import tello
from time import sleep
import Main_with_better_layout as Main

#speed variables:
global slow
slow_speed = 25
global med
med_speed = 50
global fast
fast_speed = 100



def rdq():
    print("I am here")
    save_array=Main.command_que
    array = save_array
    print(len(array))
    if len(array) !=0:
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
                print('Set speed to low')
            if speed == 'Med':
                print('Set speed to med')
            if speed == 'Fast':
                print('Set speed to fast')
            sleep(2)
            #Movement if statements
            if movement == 'Forward':
                print('Going forwards',distance,'cm')
            elif movement == 'Backwards':
                print('Going back',distance,'cm')
            elif movement == 'Left':
                print('Going left',distance,'cm')
            elif movement == 'Right':
                print('Going right',distance,'cm')
            elif movement == 'Turn Left':
                print('Turning left ',distance,'degrees')
            elif movement == 'Turn Right':
                print('Turning left',distance,'degrees')