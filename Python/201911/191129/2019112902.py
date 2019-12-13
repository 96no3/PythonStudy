import tkinter as Tk

class Frame(Tk.Frame):
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        la = Tk.Label(self, text=u"普段お使いの OS は何ですか？（複数選択可）")
        la.pack(padx=5, pady=5)
        f1 = Tk.Frame(self)
        f1.pack(padx=5, pady=5)
        self.str = Tk.StringVar()
        self.v=dict()
        for your_os in ['Unix', 'Windows', 'Mac', 'VMS', 'OS/2']:
            self.v[your_os] = Tk.IntVar()
            cb = Tk.Checkbutton(f1, text=your_os, variable=self.v[your_os], command=self.echo)
            cb.pack(side=Tk.LEFT)

        lb = Tk.Label(self, textvariable = self.str, justify=Tk.LEFT, anchor=Tk.W)
        lb.pack(padx=5, pady=5, fill=Tk.X)

    def echo(self):
        if sum ([v.get() for v in self.v.values()]) == 0:
            self.str.set(u"私はメインフレームしか使ったことがありません。")
        else:
            print(sum (v.get() for v in self.v.values()))
            str = u"私が使っている OS は、\n"
            for your_os, v in self.v.items():
                if v.get():
                    str += your_os + u"と、"
            self.str.set(str[0:-2] + u"です。")

##------------------------------------------------ 
if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()
