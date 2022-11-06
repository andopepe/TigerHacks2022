# Import the required libraries
from tkinter import *
# import rry as RA

from djitellopy import tello
from time import sleep
# Create an instance of tkinter frame or window
win=Tk()

#speed variables:
global slow
slow_speed = 25
global med
med_speed = 50
global fast
fast_speed = 100


array_position = 0
row_length = 0

class Table:
        
    def __init__(self,root):
         
        # code for creating table
        for i in range(total_rows):
            
            for j in range(total_columns+1):
       
                if j == 0:
                    self.e = Entry(root, width=2, fg='blue',
                               font=('Arial',16,'bold'))
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, i+1)
                elif j == 1:
                    self.e = Entry(root, width=9, fg='blue',
                               font=('Arial',16,'bold'))
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j-1])
                elif j == 2:
                    self.e = Entry(root, width=3, fg='blue',
                               font=('Arial',16,'bold'))
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j-1])
                elif j == 3:
                    self.e = Entry(root, width=4, fg='blue',
                               font=('Arial',16,'bold'))
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j-1])
 


# Set the size of the tkinter window
win.geometry("550x350")
global command_que
command_que=[]

# Change the label text
def show():
	label.config( text = Movement_clicked.get() )

# Dropdown menu options
options = [
	"Forward",
	"Backward",
	"Left",
	"Right",
	"Turn Left",
	"Turn Right"
]

options2 = [
	"Slow",
	"Med",
	"Fast"
    ]

lst = [(1,'Fast',19,'Forward'),
       (2,'Med',12,'Left Turn'),
       (3,'Slow', 3,'Up')
       ]
# find total number of rows and
# columns in list
total_rows = int(len(command_que)/3)
total_columns = 4



# datatype of menu text
Movement_clicked = StringVar()

# initial menu text
Movement_clicked.set( "Default" )

# datatype of menu text
Speed_clicked = StringVar()

# initial menu text
Speed_clicked.set( "Default" )




# Create Dropdown menu
Movement = OptionMenu( win , Movement_clicked , *options )
Movement.pack()


# Create button, it will change label text
# button = Button( win , text = "click Me" , command = show ).pack()


def show_total():
   sum=str(command_que)
   label.config(text=(sum+'\n'))


def add_to_list():
    distance = Distance.get()
    if distance != '' and Speed_clicked.get() != 'Default' and Movement_clicked.get() != 'Default':
        # print('Movement should be ',command_que[0][1])
        # if int(distance) < 20 or int(distance) > 500:
        #     label.config(text='Distance must be between 20 and 500')
        # else:
        command_array = [Speed_clicked.get(), Movement_clicked.get(), distance]
        command_que.append(command_array)
    
        show_total()
        global row_length
        row_length += 1
        print(command_array)
        print(command_que)
        print(row_length)
    else:
        label.config(text='All Variables must be filled or not default')

    

def array_forward():
    global promptAnswer
    promptAnswer +=3
    print(promptAnswer)
def array_back():
    global promptAnswer
    promptAnswer -=3
    print(promptAnswer)
    label.config(text=(sum+'\n'))

def new_window():
  global open 
  open = True
  win2=Tk()
  global t 
  win2.geometry("350x350")
  var = StringVar()
  var.set('0')
  l = Label(win2, textvariable = var)
  l.pack()

  t = Entry(win2, textvariable = var)
  t.pack()

  Table(win2)

  def delete():
    global t 
    global open   
    t.get()
    print('T.get is ',t.get())
    print(command_que)
    command_que.pop(int(t.get()))
    show_total()
    print('Pop success')
    open = False
    win2.destroy()
    

  Button(win2, text="Delete", command=delete).pack()
  while open:
    win2.update_idletasks()
    win2.update()




# Create an Entry widget
Label(win, text="Enter Distance (or degrees for turn)", font=('Calibri 10'))
Distance=Entry(win, width=35)
Distance.pack()




# Label(win, text="Enter Speed (Slow, Med, Fast)", font=('Calibri 10')).pack()
# Speed=Entry(win, width=35)
# Speed.pack()
Speed = OptionMenu( win , Speed_clicked , *options2 )
Speed.pack()




# Cmd_Que_Label=Label(win, text="Action list so far: ", font=('Calibri 15'))
# Cmd_Que_Label.pack(pady=20)
Button(win, text="print list", command=show_total).pack()
Button(win, text="Add to list", command=add_to_list).pack()


# Create Label
# label = Table(win)
label = Label( win , height = 5, width = 200, text = " " )
label.pack()

def rdq_visualize():

    save_array=command_que
    array = save_array
    print(array, len(array))


    
    if len(array) !=0:
        while len(array) != 0:
   
            chunk=[]
            chunk = array.pop(0)
            print('chunk = ', chunk)
            print('chunk length= ',str(len(chunk)))
            speed = chunk.pop(0)
            movement = chunk.pop(0)
            distance = chunk.pop(0)
            distance = int(distance)

            print(speed)
            print(movement)
            print(distance)
            #Speed if statements
            if speed == 'Slow':
                print('Set speed to low')
            elif speed == 'Med':
                print('Set speed to med')
            elif speed == 'Fast':
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

def run_drone_que():
    save_array=command_que
    array = save_array
    print(len(array))
    if len(array) !=0:
        me = tello.Tello()
        me.connect()
        print(me.get_battery())
        me.takeoff()
        
        while len(array) != 0:
        
            print('things left ',array)
            print(len(array))
            speed = array[0].pop(0)
            movement = array[0].pop(0)
            distance = array[0].pop(0)
            dist = distance
            dist = int(dist)
            array.pop(0)


            print(speed)
            print(movement)
            print(dist)
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
                print('Going forwards',dist,'cm')
                me.move_forward(dist)
            elif movement == 'Backwards':
                print('Going back',dist,'cm')
                me.move_back(dist)
            elif movement == 'Left':
                print('Going left',dist,'cm')
                me.move_left(dist)
            elif movement == 'Right':
                print('Going right',dist,'cm')
                me.move_right(dist)
            elif movement == 'Turn Left':
                print('Turning left ',dist,'degrees')
                me.rotate_counter_clockwise(dist)
            elif movement == 'Turn Right':
                print('Turning left',dist,'degrees')
                me.rotate_clockwise(dist)
            
        me.land()

Button(win, text="Run Drone Que", command=run_drone_que).pack() 


def stop_program():
    win.destroy()
    
    
Del= Button(win, text="Delete A Command", command=new_window)
Del.pack()

master = Tk()
def openHelpWindow():
	

    # sets the geometry of main
    # root window
    master.geometry("200x200")
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(master)

    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("500x500")

    # A Label widget to show in toplevel
    Label(newWindow, text ="To run our program successfully you need to do the following things:\n\n1.) From the drop-down menu at the top, choose your movement type\n2.) Enter the distance/rotation angle for the drone\n3.) Set the desired speed for the drone (Slow, Med, or Fast)\n4.) Hit the “Add to Que” button when you’re done\n5.) Repeat 1-4 however many times\n6.) Hit the “Run Drone Que” button to start the program\nDeleting a command\n1.) To delete a command click 'delete a command' button\n2.)Type in which command you want to delete\n3.)Click Delete ").pack()

Button(win, text="Help", command=openHelpWindow).pack()

Stop = Button(win, text="Exit the program", command=stop_program)
Stop.pack()












            






while True:
    win.update_idletasks()
    win.update()

    


