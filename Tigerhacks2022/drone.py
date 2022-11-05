import sys
import tkinter.messagebox as box
from tkinter.filedialog import asksaveasfile
global Movement_list
Forward_list ={'1' : 'FALSE','2' : 'FALSE','3' : 'FALSE'}
Backward_list ={'1' : 'FALSE','2' : 'FALSE','3' : 'FALSE'}
left_list ={'1' : 'FALSE','2' : 'FALSE','3' : 'FALSE'}
right_list ={'1' : 'FALSE','2' : 'FALSE','3' : 'FALSE'}
turn_right_list ={'1' : 'FALSE','2' : 'FALSE','3' : 'FALSE'}
turn_left_list ={'1' : 'FALSE','2' : 'FALSE','3' : 'FALSE'}
ForwardS_list ={'1' : 'FALSE','2' : 'FALSE','3' : 'FALSE'}
BackwardS_list ={'1' : 'FALSE','2' : 'FALSE','3' : 'FALSE'}
left_listS ={'1' : 'FALSE','2' : 'FALSE','3' : 'FALSE'}
right_listS ={'1' : 'FALSE','2' : 'FALSE','3' : 'FALSE'}
turn_right_listS ={'1' : 'FALSE','2' : 'FALSE','3' : 'FALSE'}
turn_left_listS ={'1' : 'FALSE','2' : 'FALSE','3' : 'FALSE'}

if sys.version_info[0] >= 3:
    import tkinter as tk
    import tkinter.ttk as ttk
else:
    import Tkinter as tk
class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #forward backward left right turn left turn right
        self.dict = {'Forward': ['1', '2', '3'],'Forward Speed' : ['10', '20', '30'],'Backward' : ['1','2','3'],'Backward Speed' : ['10','20','30']
        ,'Left': ['1','2','3'] ,'Left Speed': ['10','20','30'],'Right': ['1','2','3'],'Right Speed': ['10','20','30']
        ,'Turn left': ['1','2','3'],'Turn left speed': ['10','20','30'],'Turn right': ['1','2','3'],'Turn right speed': ['10','20','30']}
        
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


        self.button = tk.Button(self, text="Add", command=lambda : sample(self.Movement_9, self.Altitude_9))
       

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
    #box.showinfo('info', Movement_9 + ' =  ' + Altitude_9)
    print("HI")
    print(Movement_9)
    if Movement_9 == "Forward":
        print("EHELLEOEOE")
        Forward_list[Altitude_9] = Altitude_9
        print(Forward_list)
    elif Movement_9 == "Backward":
        Backward_list[Altitude_9] = Altitude_9
        print(Backward_list)
        print("BACK")
    elif Movement_9 == "Left":
        left_list[Altitude_9] = Altitude_9
        print(left_list)
        print("LEFT")
    elif Movement_9 == "Right":
        right_list[Altitude_9] = Altitude_9
        print(right_list)
        print("RIGHT")
    elif Movement_9 == "Turn right":
        turn_right_list[Altitude_9] = Altitude_9
        print(turn_right_list)
        print("Turn Right")
    elif Movement_9 == "Turn left":
        turn_left_list[Altitude_9] = Altitude_9
        print(turn_left_list)
        print("Turn Right")
    elif Movement_9 == "Forward Speed":
        print("EHELLEOEOE")
        ForwardS_list[str(int(Altitude_9)%10)] =str(int(Altitude_9)*10)
        print(ForwardS_list)
    elif Movement_9 == "Backward Speed":
        BackwardS_list[str(int(Altitude_9)%10)] = str(int(Altitude_9)*10)
        print(BackwardS_list)
        print("BACK")
    elif Movement_9 == "Left Speed":
        left_listS[str(int(Altitude_9)%10)] = str(int(Altitude_9)*10)
        print(left_listS)
        print("LEFT")
    elif Movement_9 == "Right Speed":
        right_listS[str(int(Altitude_9)%10)] = str(int(Altitude_9)*10)
        print(right_listS)
        print("RIGHT")
    elif Movement_9 == "Turn right speed":
        turn_right_listS[str(int(Altitude_9)%10)] = str(int(Altitude_9)*10)
        print(turn_right_listS)
        print("Turn Right")
    elif Movement_9 == "Turn left speed":
        turn_left_listS[str(int(Altitude_9)%10)] = str(int(Altitude_9)*10)
        print(turn_left_listS)
        print("Turn Right")
if __name__ == "__main__":
    root = tk.Tk()
    username = "root"
    password = "admin"
    app = Application(root)
    app.mainloop()