import tkinter as Tk

class Frame(Tk.Frame):
    COLS = [(u'黒', 'black'), (u'白', 'white'), (u'赤', 'red'),
            (u'緑', 'green'), (u'黄', 'yellow'), (u'青', 'blue')]

    @staticmethod
    def assoc(key, ls):
        for k, v in ls:
            if key == k:
                return v
    
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        
        self.vf = Tk.StringVar()            # 文字色
        self.vb = Tk.StringVar()            # 背景色
        self.str = Tk.StringVar()           # 表示文字列
        
        ff = Tk.LabelFrame(self, text=u'文字色')
        ff.pack(padx=5, pady=5)
        fb = Tk.LabelFrame(self, text=u'背景色')
        fb.pack(padx=5, pady=5)
        
        for jp, en in self.COLS:
            # 文字色の選択肢
            rbf = Tk.Radiobutton(ff, text=jp, variable=self.vf, value=jp, command=self.echo)
            if en == 'black':
                rbf.select()
            rbf.pack(side=Tk.LEFT)
            # 背景色の選択肢
            rbb = Tk.Radiobutton(fb, text=jp, variable=self.vb, value=jp, command=self.echo)
            if en == 'white':
                rbb.select()
            rbb.pack(side=Tk.LEFT)
            
        self.la = Tk.Label(self, textvariable=self.str, font=('Helvetica', '14', 'bold'))
        self.la.pack(padx=5, pady=5, fill=Tk.X)
        
        self.echo()

    def echo(self):
        f = self.vf.get()
        b = self.vb.get()
        self.str.set (u'%s地に%s字' % (b, f))
        self.la.configure(fg=Frame.assoc(f, self.COLS))
        self.la.configure(bg=Frame.assoc(b, self.COLS))

##------------------------------------------------ 
if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()
