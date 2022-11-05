# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("700x350")
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
   label.config(text=sum)


def add_to_list():
    distance = Distance.get()
    speed = Speed.get()
    
    # if distance != '' & speed != '':
        # print(int(distance))
    command_que.append(speed) 
    command_que.append(clicked)
    
    command_que.append(distance)
    
    # print(command_que)
    cal_sum()

# Create an Entry widget
Label(win, text="Enter Distance (or degrees for turn)", font=('Calibri 10')).pack()
Distance=Entry(win, width=35)
Distance.pack()
Label(win, text="Enter Speed (Slow, Med, Fast)", font=('Calibri 10')).pack()
Speed=Entry(win, width=35)
Speed.pack()

label=Label(win, text="Action list so far: ", font=('Calibri 15'))
label.pack(pady=20)

Button(win, text="Add to list", command=add_to_list).pack() 


while True:
    win.update_idletasks()
    win.update()

    


