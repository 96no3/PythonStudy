import tkinter as Tk

class Frame(Tk.Frame):
    """ Frame with three label """
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master, height=100, width=200)
        self.master.title('Pack Three Labels')

        # First Label
        la = Tk.Label(self, text='Hello everybody. How are you?',  bg='yellow', relief=Tk.RIDGE, bd=2)
        la.place(relx=0.02, rely=0.1, relheight=0.3, relwidth=0.95)
        # Second Label
        lb = Tk.Label(self, text='Oh My God!', bg='red', relief=Tk.RIDGE, bd=2)
        lb.place(relx=0.15, rely=0.45)
        # Third Label
        lc = Tk.Label(self, text='See you tomorrow.', bg='LightSkyBlue', relief=Tk.RIDGE, bd=2)
        lc.place(relx=0.5, rely=0.75)

if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()