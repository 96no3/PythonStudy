import tkinter as tk
import time

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
        self.pack()
        
    def create_widgets(self):
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.svar = tk.StringVar()
        self.display = tk.Label(self,
                                textvariable=self.svar,
                                font=('',30))        
        self.display.pack()
        self.btn = tk.Button(self, text='実行',command=self.start)
        self.btn.pack()

    def exec_timer(self):
        e = self.target_time - time.time()
        if e > 0:
            self.svar.set(f'あと{e}秒')
            self.after(50, self.exec_timer)
        else:
            self.svar.set('終了～！ タイムアップ!')
                   
    def start(self):
        s = self.entry.get()
        try:
            secs = int(s)
            
        except:
            self.svar.set(f'{s}は不正な数値です')
            return
        self.target_time = time.time() + secs
        self.exec_timer()
    
root = tk.Tk()
root.title('いいかげんなタイマー(ちゃんと直してね)')
app = Application(root)
app.mainloop()