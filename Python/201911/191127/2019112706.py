#! /usr/bin/env python

import tkinter as Tk
import os

BLUE = '#99CCFF'
YELLOW = '#FFCC00'
RED = '#FF00FF'
CLOCK = os.path.dirname(__file__)+"/meza-bl-2.gif"

class Frame(Tk.Frame):
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        
        self.echo = Tk.StringVar()
        self.m = 3
        self.echo_set()

        self.master.title('Alarm')
        f_display = Tk.Frame(self, relief=Tk.RIDGE, bd=4)
        f_display.pack(fill=Tk.X, expand=1)

        self.image= Tk.PhotoImage(file=CLOCK)
        self.icon=Tk.Label(f_display, image=self.image, bg=BLUE)
        self.icon.grid(row=0,column=0, rowspan=2)
        display = Tk.Label(f_display, textvariable=self.echo, width=5, relief=Tk.SUNKEN, bd=2, anchor = Tk.E, 
                             font=('Helvetica', '24'), bg='white')
        display.grid(row=0, column=1, rowspan=2, sticky=Tk.N+Tk.S)
        self.b_inc = Tk.Button(f_display, font=('Helvetica', '6'), text='+', command=self.inc_time)
        self.b_inc.grid(row=0, column=2, sticky=Tk.W + Tk.E + Tk.S, pady=1)
        self.b_dec = Tk.Button(f_display, font=('Helvetica', '6'), text='-', command=self.dec_time)
        self.b_dec.grid(row=1, column=2, sticky=Tk.W + Tk.E + Tk.N, pady=1)

        f_button = Tk.Frame(self)
        f_button.pack(pady=2)
        self.b_start = Tk.Button(f_button, text='Start', command=self.start)
        self.b_stop = Tk.Button(f_button, text='Stop', command=self.stop, state=Tk.DISABLED)
        self.b_reset = Tk.Button(f_button, text='Reset', command=self.reset, state=Tk.DISABLED)
        self.b_start.pack(side=Tk.LEFT, padx=1)
        self.b_stop.pack(side=Tk.LEFT, padx=1)
        self.b_reset.pack(side=Tk.LEFT, padx=1)
        
    def echo_set(self):
        self.timer = 60 * self.m
        self.echo.set('%02d:00' % (self.m))

    def inc_time(self):
        self.m += 1
        self.echo_set()

    def dec_time(self):
        self.m -= 1
        self.echo_set()

    def start(self):
        self.started = True
        if 0<self.timer<=20:
            self.icon.configure(bg=YELLOW)
        elif(0 >= self.timer):
            self.icon.configure(bg=RED)
        self.after(1000, self.counting)
        self.b_start.configure(state=Tk.DISABLED)
        self.b_stop.configure(state=Tk.NORMAL)
        self.b_reset.configure(state=Tk.DISABLED)
        self.b_inc.configure(state=Tk.DISABLED)
        self.b_dec.configure(state=Tk.DISABLED)
        

    def stop(self):
        self.icon.configure(bg=BLUE)
        self.started = False
        self.b_start.configure(state=Tk.NORMAL)
        self.b_stop.configure(state=Tk.DISABLED)
        self.b_reset.configure(state=Tk.NORMAL)

    def reset(self):
        self.echo_set()
        self.b_reset.configure(state=Tk.DISABLED)
        self.b_inc.configure(state=Tk.NORMAL)
        self.b_dec.configure(state=Tk.NORMAL)

    def counting(self):
            if self.started:
                self.timer -=1
                self.echo.set('%02d:%02d' % (self.timer/60, self.timer%60))
                if self.timer == 20:
                    self.icon.configure(bg=YELLOW)

                if self.timer <= 0:
                    self.bell()
                    t= -1 * self.timer
                    self.icon.configure(bg=RED)
                    self.echo.set('-%02d:%02d' % (t/60, t%60))
                    self.after(500, self.yellow)
                    
                self.after(1000, self.counting)

    def yellow(self):
        if self.started:
            self.icon.configure(bg=YELLOW)

if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()
