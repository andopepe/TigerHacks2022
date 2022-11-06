# Import the required libraries
from tkinter import *
import Read_Array as RA
from djitellopy import tello
from time import sleep
# Create an instance of tkinter frame or window
win=Tk()

global array_spot

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
	label.config( text = clicked.get() )

# Dropdown menu options
options = [
	"Forward",
	"Backward",
	"Left",
	"Right",
	"Turn Left",
	"Turn Right"
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set( "Default" )

# Create Dropdown menu
Movement = OptionMenu( win , clicked , *options )
Movement.pack()

# Create button, it will change label text
# button = Button( win , text = "click Me" , command = show ).pack()

# Create Label
label = Label( win , text = " " )
label.pack()



def cal_sum():
   t1= Distance.get()
   t2= Speed.get()
   sum=str(command_que)#+ ' ['+t1+' '+ t2+']'
   label.config(text=(sum+'\n'))


def add_to_list():
    distance = Distance.get()
    speed = Speed.get()
    
    # if distance != '' & speed != '':
        # print(int(distance))
    command_que.append(speed) 

    command_que.append(clicked)
    
    command_que.append(distance)
    array_forward()
    # print(command_que)
    cal_sum()

def array_forward():
    array_spot+=3
def array_back():
    array_spot-=3

# Create an Entry widget
Label(win, text="Enter Distance (or degrees for turn)", font=('Calibri 10')).pack()
Distance=Entry(win, width=35)
Distance.pack()


Label(win, text="Enter Speed (Slow, Med, Fast)", font=('Calibri 10')).pack()
Speed=Entry(win, width=35)
Speed.pack()

Cmd_Que_Label=Label(win, text="Action list so far: ", font=('Calibri 15'))
Cmd_Que_Label.pack(pady=20)

Button(win, text="Add to list", command=add_to_list).pack()

Button(win, text="Run Drone Que", command=RA.run_drone_que(command_que)).pack() 


while True:
    win.update_idletasks()
    win.update()

    


