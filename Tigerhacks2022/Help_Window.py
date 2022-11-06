# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *

# creates a Tk() object
master = Tk()

# sets the geometry of main
# root window
master.geometry("200x200")


# function to open a new window
# on a button click
def openNewWindow():
	
	# Toplevel object which will
	# be treated as a new window
	newWindow = Toplevel(master)

	# sets the title of the
	# Toplevel widget
	newWindow.title("New Window")

	# sets the geometry of toplevel
	newWindow.geometry("500x500")

	# A Label widget to show in toplevel
	Label(newWindow, text ="To run our program successfully you need to do the following things:\n1.) From the drop-down menu at the top, choose your movement type\n2.) Enter the distance/rotation angle for the drone\n3.) Set the desired speed for the drone (Slow, Med, or Fast)\n4.) Hit the “Add to Que” button when you’re done\n5.) Repeat 1-4 however many times\n6.) Hit the “Run Drone Que” button to start the program").pack()


label = Label(master, text ="This is the main window")

label.pack(pady = 10)

# a button widget which will open a
# new window on button click
btn = Button(master, text ="Click to open a new window", command = openNewWindow)
btn.pack(pady = 10)

# mainloop, runs infinitely
mainloop()
