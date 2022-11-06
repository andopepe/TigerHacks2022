import sys
import tkinter.messagebox as box
from tkinter.filedialog import asksaveasfile
if sys.version_info[0] >= 3:
    import tkinter as tk
    import tkinter.ttk as ttk
else:
    import Tkinter as tk


class App(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.dict = {'Asia': ['Japan', 'China', 'Malaysia'],
                     'Europe': ['Germany', 'France', 'Switzerland']}

        self.variable_a = tk.StringVar(self)
        self.variable_b = tk.StringVar(self)
        self.last_county = tk.StringVar(self)
        self.area = tk.StringVar(self)
        self.country = tk.StringVar(self)

        self.variable_b.trace('w', self.fun2)
        self.variable_a.trace('w', self.update_options)


        self.combobox_a = ttk.Combobox(self, values=list(self.dict.keys()), state='readonly')
        self.combobox_a.bind("<<ComboboxSelected>>", self.fun)
        self.combobox_a.current(0)
        self.combobox_b = ttk.Combobox(self, values=self.dict['Asia'], state='readonly')
        self.combobox_b.bind("<<ComboboxSelected>>", self.fun2)
        self.combobox_b.current(0)


        username = self.fun()
        password = self.fun2()


        self.button = tk.Button(self, text="Login", command=lambda : sample(username, password, self.area, self.country))


        # self.variable_a.set('Asia')

        self.combobox_a.pack()
        self.combobox_b.pack()
        self.button.pack()
        self.pack()

    def fun(self,*args):
        print("changed 1-st combobox value to: " + self.combobox_a.get())
        if self.last_county != self.combobox_a.get():
            self.combobox_b['values']=self.dict[self.combobox_a.get()]
            self.combobox_b.current(0)
        self.last_county = self.area = self.combobox_a.get()
        return self.variable_a.get()

    def fun2(self, *args):
        print("changed 2-nd combobox value to" + self.combobox_b.get())
        self.country = self.combobox_b.get()
        return self.variable_b.get()

    def update_options(self, *args):
        countries = self.dict[self.variable_a.get()]
        self.variable_b.set(countries[0])

        menu = self.combobox_b['menu']
        menu.delete(0, 'end')

        for country in countries:
            menu.add_command(label=country, command=lambda nation=country: self.variable_b.set(nation))


def sample(username, password, area, country):
    box.showinfo('info', 'Selected area: ' + area + '\nSelected country: ' + country + '\nEnter Credentials')

if __name__ == "__main__":
    root = tk.Tk()
    username = "root"
    password = "admin"
    app = App(root)
    app.mainloop()