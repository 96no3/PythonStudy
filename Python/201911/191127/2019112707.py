#! /usr/bin/env python

import tkinter as Tk
import os

FLOWER = os.path.dirname(__file__)+"/nanohana3.gif"

class Frame(Tk.Frame):
    
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.master.title('select background')
        f_button = Tk.Frame(self)
        f_button.pack(side=Tk.LEFT, padx=5, pady=5)
        self.flower = Tk.PhotoImage(file=FLOWER)
        self.label = Tk.Label(self, image=self.flower, relief=Tk.RAISED, bd=3)
        self.label.pack(side=Tk.RIGHT, padx =5)

        b_cornsilk = Tk.Button(f_button, text='cornsilk',  bg='#FFF8DC', command=self.c_cornsilk)
        b_khaki = Tk.Button(f_button, text='khaki',  bg='#F0E68C', command=self.c_khaki)
        b_lightgreen = Tk.Button(f_button, text='lightgreen',  bg='#90EE90', command=self.c_lightgreen)
        b_lightpink = Tk.Button(f_button, text='lightpink',  bg='#FFB6C1', command=self.c_lightpink)
        b_lightskyblue = Tk.Button(f_button, text='lightskyblue',  bg='#87CEFA', command=self.c_lightskyblue)
        b_palegreen = Tk.Button(f_button, text='palegreen',  bg='#98FB98', command=self.c_palegreen)
        b_azure = Tk.Button(f_button, text='azure',  bg='#F0FFFF', command=self.c_azure)
        b_aliceblue = Tk.Button(f_button, text='aliceblue',  bg='#F0F8FF', command=self.c_aliceblue)
        b_beige = Tk.Button(f_button, text='beige',  bg='#F5F5DC', command=self.c_beige)

        b_aliceblue.pack(fill=Tk.X)
        b_azure.pack(fill=Tk.X)
        b_beige.pack(fill=Tk.X)
        b_cornsilk.pack(fill=Tk.X)
        b_khaki.pack(fill=Tk.X)
        b_lightgreen.pack(fill=Tk.X)
        b_lightpink.pack(fill=Tk.X)
        b_lightskyblue.pack(fill=Tk.X)
        b_palegreen.pack(fill=Tk.X)

    def c_cornsilk(self):
        self.label.configure(bg='#FFF8DC')

    def c_khaki(self):
        self.label.configure(bg='#F0E68C')

    def c_lightgreen(self):
        self.label.configure(bg='#90EE90')

    def c_lightpink(self):
        self.label.configure(bg='#FFB6C1')

    def c_lightskyblue(self):
        self.label.configure(bg='#87CEFA')

    def c_palegreen(self):
        self.label.configure(bg='#98FB98')

    def c_azure(self):
        self.label.configure(bg='#F0FFFF')

    def c_aliceblue(self):
        self.label.configure(bg='#F0F8FF')

    def c_beige(self):
        self.label.configure(bg='#F5F5DC')


#########################################
# 
# cornsilk
# #FFF8DC
# 
# khaki
# #F0E68C
# 
# lightgreen
# #90EE90
# 
# lightpink
# #FFB6C1
# 
# lightskyblue
# #87CEFA
# 
# palegreen
# #98FB98
# 
# azure
# #F0FFFF
# 
# aliceblue
# #F0F8FF
# 
# beige
# #F5F5DC
#########################################
##------------------------------------------------ 

if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()
