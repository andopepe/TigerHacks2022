from tkinter import *

master = Tk()

variable = StringVar(master)
variable.set("one") # default value

w = OptionMenu(master, variable, "one", "two", "three")
w.pack()

print(w.__getitem__('one'))



while True:
    master.update_idletasks()
    master.update()