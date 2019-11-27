#! /usr/bin/env python

import tkinter as Tk
import os

FLOWER = os.path.dirname(__file__)+"/nanohana3.gif"

BGS = [('aliceblue', '#F0F8FF'), ('azure', '#F0FFFF'), ('beige', '#F5F5DC'),              \
       ('cornsilk', '#FFF8DC'), ('khaki', '#F0E68C'), ('lightgreen', '#90EE90'),          \
       ('lightpink', '#FFB6C1'), ('lightskyblue', '#87CEFA'), ('palegreen', '#98FB98')]

class Button(Tk.Button):
    def __init__(self, master, label, color_name, color_code):
        Tk.Button.__init__(self, master, text=color_name, bg=color_code, command=self.bg_change)
        self.label = label
        self.color_code = color_code

    def bg_change(self):
        self.label.configure(bg=self.color_code)

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
            b = Button(f_button, label, name, code)
            b.pack(fill=Tk.X)

if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()
