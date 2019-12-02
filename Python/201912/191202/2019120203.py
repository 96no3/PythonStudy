import tkinter as Tk

class Mtop:
    def __init__(self, master):
        self.master = master

    def __call__(self, event=None):
        top = Tk.Toplevel(self.master)
        f = Tk.Frame(top)
        f.pack()
        la = Tk.Label(f, text=self.master and u'子供' or u'他人', font =('Helvetica', '12'))
        la.pack()
        lb = Tk.Label(f, text=self.master and u'この Toplevel は親フレームとともに消えます。' or
                                              u'この Toplevel は親フレームが消えても残ります。' )
        lb.pack()

class Frame(Tk.Frame):
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        l = Tk.Label(self, text=u'下のボタンを押して、下の \'親フレーム\' と親子関係にある TopLevel と \n'
                     u'独立した Toplevel を作成してください。\n'
                     u'それから、\'親フレームを消す\'ボタンを押すと、\n親フレームと、親子関係にある Toplevel が消え、\n'
                     u'独立した Toplebel は残ります。', justify=Tk.LEFT)
        l.pack(padx=10, pady=5)
        f = Tk.LabelFrame(self, text=u'親フレーム')
        f.pack(padx=10, pady=5)
        bc = Tk.Button(f, text=u'親フレームの子供のトップレベルを作成', command=Mtop(f))
        bc.pack(fill=Tk.X, pady=5, padx=10)
        bn = Tk.Button(f, text=u'他人のトップレベルを作成', command=Mtop(None))
        bn.pack(fill=Tk.X, pady=5, padx=10)
        bd = Tk.Button(f, text=u'親フレームを消す', command=f.destroy)
        bd.pack(fill=Tk.X, pady=5, padx=10)      

##------------------------------------------------ 
if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()
