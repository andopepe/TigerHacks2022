import sys
import tkinter.messagebox as box
from tkinter.filedialog import asksaveasfile
global Movement_list
Movement_list ={'A' : 'FALSE','B' : 'FALSE','C' : 'FALSE','D' : 'FALSE'}
if sys.version_info[0] >= 3:
    import tkinter as tk
    import tkinter.ttk as ttk
else:
    import Tkinter as tk
class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #forward backward left right turn left turn right
        self.dict = {'Forward': ['A', 'B', 'C','D'],'Backward' : ['1','2','3','4','5']
        ,'Left': ['1','2','3','4','5'],'Right': ['1','2','3','4','5'],'Turn left': ['1','2','3','4','5'],'Turn right': ['1','2','3','4','5']}

        self.Movement = tk.StringVar(self)
        self.Alititude = tk.StringVar(self)
        self.last_Altitude = tk.StringVar(self)
        self.Movement_9 = tk.StringVar(self)
        self.Altitude_9 = tk.StringVar(self)

        self.Alititude.trace('w', self.fun2)
        self.Movement.trace('w', self.update_options)

        
        self.Move = ttk.Combobox(self, values=list(self.dict.keys()), state='readonly')
        self.Move.bind("<<ComboboxSelected>>", self.fun)
        self.Move.current(0)
        self.Alti = ttk.Combobox(self, values=self.dict['Forward'], state='readonly')
        self.Alti.bind("<<ComboboxSelected>>", self.fun2)
        self.Alti.current(0)


        username = self.fun()
        password = self.fun2()


        self.button = tk.Button(self, text="Login", command=lambda : sample(self.Movement_9, self.Altitude_9))
       

        # self.Movement.set('Asia')

        self.Move.pack()
        self.Alti.pack()
        self.button.pack()
        self.pack()

    def fun(self,*args):
        print("OPTIONS CHANGED combobox value to: " + self.Move.get())
        if self.last_Altitude != self.Move.get():
            self.Alti['values']=self.dict[self.Move.get()]
            self.Alti.current(0)
        self.last_Altitude = self.Movement_9 = self.Move.get()
        return self.Movement.get()
        
    def fun2(self, *args):
        print("CHOICES CHANGED combobox value to: " + self.Alti.get())
        self.Altitude_9 = self.Alti.get()
        return self.Alititude.get()

    def update_options(self, *args):
        countries = self.dict[self.Movement.get()]
        self.Alititude.set(countries[0])

        menu = self.Alti['menu']
        menu.delete(0, 'end')

        for Altitude_9 in countries:
            menu.add_command(label=Altitude_9, command=lambda nation=Altitude_9: self.Alititude.set(nation))
            

def sample(Movement_9, Altitude_9):
   # box.showinfo('info', 'Selected Movement_9: ' + Movement_9 + '\nSelected Altitude_9: ' + Altitude_9 + '\nEnter Credentials')
    print("HI")
    if True:
        print("EHELLEOEOE")
        Movement_list[Altitude_9] = 'TRUE'
        print(Movement_list)

if __name__ == "__main__":
    root = tk.Tk()
    
    username = "root"
    password = "admin"
    app = Application(root)
   
    app.mainloop()