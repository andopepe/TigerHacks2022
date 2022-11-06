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

    command_que.append('Forward')
    command_que.append(distance)

    # print(command_que)
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

# global promptAnswer
#   promptAnswer=0
#   def delete(promptAnswer):
#     int(promptAnswer)
#     command_que.pop(promptAnswer)
#     command_que.pop(promptAnswer+1)
#     command_que.pop(promptAnswer+2)
#     print(command_que)

#   win2=Tk()
#   win2.geometry("350x350")
#   global array_length
#   print(array_length)
    # Button(win2, text="Delete", command=delete(promptAnswer)).pack()
#   Button(win2, text="---", command=array_back).pack()
#   Button(win2, text="+++", command=array_forward).pack()
#   Label(win2, text="which command would you like to delete?", font = ('Calibri 10')).pack()
#   lbl = Label(win2, text=promptAnswer, font = ('Calibri 10'))
#   lbl.config(text=str(promptAnswer))
#   lbl.pack()
#   win2.update_idletasks()
#   win2.update()



  


  

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

Button(win, text="change command", command=edit_list).pack()
while True:
    win.update_idletasks()
    win.update()

    


