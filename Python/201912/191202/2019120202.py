import tkinter as Tk


class Frame(Tk.Frame):
    CONSTELLATIONS = ( u'水瓶座', u'魚　座', u'牡羊座', u'牡牛座', u'双子座', u'蟹　座', u'獅子座',
                   u'乙女座', u'天秤座', u'蠍　座', u'射手座', u'山羊座')
    
    BLOOD = ('A', 'B', 'O', 'AB')

    FORTUNE = [u'大吉', u'中吉', u'吉', u'凶']

    @staticmethod
    def position(obj, tup):
        for i, o in enumerate(tup):
            if o==obj:
                return i

    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        info = Tk.Label(self, text=u'Spinbox を使ったイカサマ占い。')
        info.pack(padx=5, pady=5)
        f = Tk.Frame(self)
        f.pack(padx=5, pady=5)
        lb=Tk.Label(f, text=u'血液型')
        lb.grid(row=0, column=0, padx=5, pady=5)
        self.sb=Tk.Spinbox(f, values=Frame.BLOOD)
        self.sb.grid(row=0, column=1, padx=5, pady=5)
        lc=Tk.Label(f, text=u'星座')
        lc.grid(row=1, column=0, padx=5, pady=5)
        self.sc = Tk.Spinbox(f, values=Frame.CONSTELLATIONS)
        self.sc.grid(row=1, column=1, padx=5, pady=5)
        b=Tk.Button(self, text=u'占う', command=self.tell_fortune)
        b.pack(padx=5, pady=5)
        self.fortune=Tk.StringVar()
        lf = Tk.Label(self, textvariable=self.fortune, fg='red', font=('Helvetica', '14', 'bold'))
        lf.pack(padx=5, pady=5)

    def tell_fortune(self):
        i = Frame.position(self.sb.get(), Frame.BLOOD) + 1
        j = Frame.position(self.sc.get(), Frame.CONSTELLATIONS) + 1
        self.fortune.set(Frame.FORTUNE[(i*j*j)%4])    

##------------------------------------------------
if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()