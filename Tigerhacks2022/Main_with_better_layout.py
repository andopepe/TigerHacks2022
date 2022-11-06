# Import the required libraries
from tkinter import *
import rry as RA
from djitellopy import tello
from time import sleep
# Create an instance of tkinter frame or window
win=Tk()


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
        if int(distance) < 20 or int(distance) > 500:
            label.config(text='Distance must be between 20 and 500')
        else:
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

Rdq = Button(win, text="Run Drone Que", command='RA.run_drone_que')
Rdq.pack()


def stop_program():
    win.destroy()
    
    
Del= Button(win, text="Delete A Command", command=new_window)
Del.pack()
Stop = Button(win, text="Exit the program", command=stop_program)
Stop.pack()



while True:
    win.update_idletasks()
    win.update()

    


