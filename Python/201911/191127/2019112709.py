#! /usr/bin/env python

import tkinter as Tk
import os

FLOWER = os.path.dirname(__file__)+"/nanohana3.gif"

BGS = [('aliceblue', '#F0F8FF'), ('azure', '#F0FFFF'), ('beige', '#F5F5DC'),              \
       ('cornsilk', '#FFF8DC'), ('khaki', '#F0E68C'), ('lightgreen', '#90EE90'),          \
       ('lightpink', '#FFB6C1'), ('lightskyblue', '#87CEFA'), ('palegreen', '#98FB98')]

class BgChange:
    def __init__(self, label, color):
        self.label = label
        self.color = color

    def __call__(self, event=None):
        self.label.configure(bg=self.color)

class Frame(Tk.Frame):    
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.master.title('select background')
        f_button = Tk.Frame(self)
        f_button.pack(side=Tk.LEFT, padx=5, pady=5)
        self.flower = Tk.PhotoImage(file=FLOWER)
        label = Tk.Label(self, image=self.flower, relief=Tk.RAISED, bd=3)
        label.pack(side=Tk.RIGHT, padx =5)

        for name, code in BGS:
            b = Tk.Button(f_button, text=name, bg=code, command=BgChange(label, code))
            b.pack(fill=Tk.X)

if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()
