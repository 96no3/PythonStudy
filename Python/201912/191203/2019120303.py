import time as t
import tkinter as tk

class ClockApp(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master.title('Clock')
        self.master.geometry("180x30")
        self.clock = tk.StringVar()
        self.counting()
        self.label = tk.Label(self, textvariable=self.clock, relief=tk.SUNKEN, bg='white')
        self.label.pack()

    def clock_set(self):
        self.clock.set(t.strftime("%T"))

    def counting(self):
        self.clock_set()
        self.after(250, self.counting)

if __name__ == '__main__':
    app = ClockApp()
    app.pack()
    app.mainloop()          
