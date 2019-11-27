#! /usr/bin/env python

import tkinter as Tk
import os

FLOWER = os.path.dirname(__file__)+"/nanohana3.gif"

BGS = [('aliceblue', '#F0F8FF'), ('azure', '#F0FFFF'), ('beige', '#F5F5DC'),              \
       ('cornsilk', '#FFF8DC'), ('khaki', '#F0E68C'), ('lightgreen', '#90EE90'),          \
       ('lightpink', '#FFB6C1'), ('lightskyblue', '#87CEFA'), ('palegreen', '#98FB98')]

class Frame(Tk.Frame):    
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.master.title('select background')
        f_button = Tk.Frame(self)
        f_button.pack(side=Tk.LEFT, padx=5, pady=5)
        self.flower = Tk.PhotoImage(file=FLOWER)
        self.label = Tk.Label(self, image=self.flower, relief=Tk.RAISED, bd=3)
        self.label.pack(side=Tk.RIGHT, padx =5)

        for name, code in BGS:
            b = Tk.Button(f_button, text=name, bg=code, command=self.bgchange(code))
            b.pack(fill=Tk.X)
    
    def bgchange(self,color):
        def f():
            self.label.configure(bg=color)
        return f

if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()
