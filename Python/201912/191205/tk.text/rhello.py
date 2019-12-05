#! /usr/bin/env python

import tkinter as Tk
import random as R

class Label(Tk.Label):
    def __init__(self, master=None, **key):
        key['text']='Hello world!'
        key['font']=('Helvetica', '24', 'bold')
        Tk.Label.__init__(self, master, **key)
        self.bind('<1>', self.bg_change)
    
    def bg_change(self, event):
        r = R.randint(0,255)
        g = R.randint(0,255)
        b = R.randint(0,255)
        self.configure(bg='#%02X%02X%02X' % (r, g, b))

if __name__ == '__main__':
    l = Label()
    l.pack()
    l.mainloop()
