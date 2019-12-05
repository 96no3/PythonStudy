#! /usr/bin/env python

import tkinter as Tk
import bbr as B

class Frame(Tk.Frame):
    def __init__(self, master=None, **key):
        Tk.Frame.__init__(self, master, **key)
        self.label=Tk.Label(self, text='click me!', width=32, height=2, font=('Helvetica', '8'), fg='white', bg='black')
        self.label.pack(fill=Tk.BOTH)
        self.label.bind('<1>', self.heating_start)
        self.label.bind('<3>', self.reset)

    def heating_start(self, event):
        self.temp=1000
        self.label.configure(width=12, height=1, text='Hello world!', font=('Helvetica', '24'), bg='black')
        self.after(100, self.heating)

    def heating(self):
        self.label.configure(fg=B.bbrcolor_rel(self.temp))
        self.temp += 50
        if self.temp < 8000:
            self.after(100, self.heating)
        else:
            self.label.configure(fg='black', bg='red')

    def reset(self, event):
        self.label.configure(text='click me!', width=32, height=2, font=('Helvetica', '8'), fg='white', bg='black')

if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()
