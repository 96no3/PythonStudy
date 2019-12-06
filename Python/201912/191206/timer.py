import tkinter as tk
import time,os

PATH = os.path.dirname(__file__)+"/"

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('Timer')
        self.master.geometry('500x220')
        self.target_time = None      
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self, text="カウントダウンタイマー",bg="lightgreen").pack(fill=tk.X,expand=1)
        
        f_input = tk.Frame(self, relief=tk.RIDGE, bd=4)
        f_input.pack(fill=tk.X, expand=1)
        f_entry = tk.Frame(f_input)
        f_entry.pack(side=tk.LEFT)
        tk.Label(f_entry,text="時間（秒）").pack()
        self.entry = tk.Entry(f_entry)
        self.entry.insert(tk.END,"60")
        self.entry.pack()
        f_btn1 = tk.Frame(f_input)
        f_btn1.pack(side=tk.RIGHT)
        self.img0 = tk.PhotoImage(file=PATH+"noodle.png")
        self.b_3m = tk.Button(f_btn1, image=self.img0, command=self.set_3m)
        self.img1 = tk.PhotoImage(file=PATH+"udon.png")
        self.b_5m = tk.Button(f_btn1, image=self.img1, command=self.set_5m)
        self.b_5m.pack(side=tk.RIGHT,padx=5)        
        self.b_3m.pack(side=tk.RIGHT,padx=5)        
        
        self.svar = tk.StringVar()
        self.time_init()
        self.display = tk.Label(self, textvariable=self.svar, relief=tk.SUNKEN,
                              font=("",20),bg='white')        
        self.display.pack(fill=tk.X,expand=1)

        f_btn2 = tk.Frame(self, relief=tk.RIDGE, bd=4)
        f_btn2.pack(fill=tk.X,expand=1)
        self.image1 = tk.PhotoImage(file=PATH+"start.png")
        self.b_start = tk.Button(f_btn2, image=self.image1, command=self.start)
        self.image2 = tk.PhotoImage(file=PATH+"stop.png")
        self.b_stop = tk.Button(f_btn2, image=self.image2, command=self.stop, state=tk.DISABLED)
        self.image3 = tk.PhotoImage(file=PATH+"reset.png")
        self.b_reset = tk.Button(f_btn2, image=self.image3, command=self.reset, state=tk.DISABLED)
        self.b_start.pack(side=tk.LEFT, padx=10)
        self.b_stop.pack(side=tk.LEFT, padx=10)
        self.b_reset.pack(side=tk.LEFT, padx=10)       

    def time_init(self):
        self.svar.set("セットする時間を秒単位で入力してください。")

    def time_err(self,s):
        self.svar.set(f'{s}は不正な数値です。')        

    def time_set(self):
        self.h = self.target_time // 3600
        self.m = (self.target_time % 3600) // 60
        self.s = (self.target_time % 3600) % 60        
        self.svar.set("のこり %02d時間 %02d分 %02d秒" % (self.h,self.m,self.s))

    def time_finish(self):
        self.svar.set('終了～！ タイムアップ!')

    def deltatime(self):
        return (time.time() - self.pretime)

    def set_3m(self):
        self.entry.delete(0,tk.END)
        self.entry.insert(tk.END,"180")

    def set_5m(self):
        self.entry.delete(0,tk.END)
        self.entry.insert(tk.END,"300")

    def start(self):
        try:
            if not self.target_time:
                self.target_time = int(self.entry.get())                                   
        except:
            self.time_err(self.entry.get())
            return

        self.started = True
        self.pretime = time.time()
        self.time_set()
        if(0 < self.target_time <= 10):
            self.display.config(bg="red")        
        self.entry.config(state=tk.DISABLED)
        self.b_start.config(state=tk.DISABLED)
        self.b_stop.config(state=tk.NORMAL)
        self.b_reset.config(state=tk.DISABLED)
        self.b_3m.config(state=tk.DISABLED) 
        self.b_5m.config(state=tk.DISABLED)
        self.exec_timer()
 
    def stop(self):
        self.started = False
        self.b_start.config(state=tk.NORMAL)
        self.b_stop.config(state=tk.DISABLED)
        self.b_reset.config(state=tk.NORMAL)
 
    def reset(self):
        self.target_time = None
        self.time_init()
        self.display.config(bg="white")
        self.b_reset.config(state=tk.DISABLED)
        self.entry.configure(state=tk.NORMAL)
        self.b_3m.config(state=tk.NORMAL) 
        self.b_5m.config(state=tk.NORMAL) 
        self.b_start.config(state=tk.NORMAL)

    def finish(self):
        self.started = False
        self.time_finish()
        self.b_start.config(state=tk.DISABLED)
        self.b_stop.config(state=tk.DISABLED)
        self.b_reset.config(state=tk.NORMAL)
 
    def exec_timer(self):
        if self.started:
            self.target_time = self.target_time - self.deltatime()
            self.time_set()

            if (0 < self.target_time <= 10):
                self.display.config(bg="red")

            if self.target_time <= 0:
                self.finish()

            self.pretime = time.time()
            self.after(50, self.exec_timer)

if __name__ == '__main__':
    app = Application()
    app.pack()
    app.mainloop()