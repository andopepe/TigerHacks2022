# Import the required libraries
from tkinter import *
import Read_Array as RA
from djitellopy import tello
from time import sleep
# Create an instance of tkinter frame or window
win=Tk()


array_position = 0
array_length = 0

class Table:
    def __init__(self,root):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])


# Set the size of the tkinter window
win.geometry("350x350")
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

# Create Label
label = Label( win , text = " " )
label.pack()



def cal_sum():
   t1= Distance.get()
#    t2= Speed.get()
   sum=str(command_que)#+ ' ['+t1+' '+ t2+']'
   label.config(text=(sum+'\n'))


def add_to_list():
    distance = Distance.get()
    if distance != '' and Speed_clicked.get() != 'Default' and Movement_clicked.get() != 'Default':
        command_que.append(Speed_clicked.get()) 
        command_que.append(Movement_clicked.get())
        command_que.append(distance)

        cal_sum()
        global array_length
        array_length += 3
        print(array_length)
    

def array_forward():
    global promptAnswer
    promptAnswer +=3
    print(promptAnswer)
def array_back():
    global promptAnswer
    promptAnswer -=3
    print(promptAnswer)
    label.config(text=(sum+'\n'))

def edit_list():
  
  win2=Tk()
  global t 
  win2.geometry("350x350")
  var = StringVar()
  var.set('0')
  l = Label(win2, textvariable = var)
  l.pack()

  t = Entry(win2, textvariable = var)
  t.pack()
  def delete():
    global t    
    t.get()
    print(t.get())
    command_que.pop(int(t.get()))
    command_que.pop(int(t.get()))
    command_que.pop(int(t.get()))
    print(command_que)

  Button(win2, text="Delete", command=delete).pack()
  while True:
    win2.update_idletasks()
    win2.update()




# Create an Entry widget
Label(win, text="Enter Distance (or degrees for turn)", font=('Calibri 10')).pack()
Distance=Entry(win, width=35)
Distance.pack()


# Label(win, text="Enter Speed (Slow, Med, Fast)", font=('Calibri 10')).pack()
# Speed=Entry(win, width=35)
# Speed.pack()
Speed = OptionMenu( win , Speed_clicked , *options2 )
Speed.pack()


Cmd_Que_Label=Label(win, text="Action list so far: ", font=('Calibri 15'))
Cmd_Que_Label.pack(pady=20)
Button(win, text="print list", command=cal_sum).pack()
Button(win, text="Add to list", command=add_to_list).pack()
Button(win, text="Run Drone Que", command=RA.run_drone_que(command_que)).pack() 

Button(win, text="Delete A Command", command=edit_list).pack()
while True:
    win.update_idletasks()
    win.update()

    


