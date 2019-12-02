import tkinter as Tk    
    
class Frame(Tk.Frame):
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        info = Tk.Label(self, text=u'スケールをいじってフレームの色を変えてください。', font=('Helvetica', '12', 'bold'))
        info.pack(padx=10, pady=5)
        f = Tk.Frame(self)
        f.pack(padx=5, pady=5)
        self.sc = dict()
        for i, color in enumerate(['red', 'green', 'blue']):
            la = Tk.Label(f, text=Frame.e2j(color), fg=color, font=('Helvetica', '12', 'bold'))
            la.grid(row=0, column=i, padx=10, pady=5)
            self.sc[color] = Tk.Scale(f, from_=0, to=255, length=150, bd=0, 
                                      command=self.change_bg, tickinterval=50, orient=Tk.VERTICAL)
            self.sc[color].set(255)
            self.sc[color].grid(row=1, column=i, padx=10, pady=5)            

    def change_bg(self, event):
        color = '#%02X%02X%02X' % (self.sc['red'].get(), self.sc['green'].get(), self.sc['blue'].get())
        Frame.change_bg_rec(self, color)

    @staticmethod
    def change_bg_rec(item, color):
        item.configure(bg=color)
        for child in item.winfo_children():
            Frame.change_bg_rec(child, color)

    @staticmethod
    def e2j(en):
        if en=='red':
            return u'赤'
        elif en=='green':
            return u'緑'
        else:
            return u'青'

##------------------------------------------------ 
if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()