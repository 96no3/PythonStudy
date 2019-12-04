import tkinter as tk 

class TimerApp(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title('Timer')
        self.master.geometry('500x170')
        self.count = None
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self, text="カウントダウンタイマー",bg="lightgreen").pack(fill=tk.X)
        tk.Label(self,text="時間（秒）").pack()
        self.entry = tk.Entry(self)
        self.entry.insert(tk.END,"60")
        self.entry.pack() 
        self.time = tk.StringVar()
        self.time_init()
        self.label = tk.Label(self, textvariable=self.time, relief=tk.SUNKEN,
                              font=("",20),bg='white')
        self.label.pack(fill=tk.X,pady=10)
        f_button = tk.Frame(self)
        f_button.pack()
        self.b_start = tk.Button(f_button, text='Start', font=("",15), command=self.start)
        self.b_stop = tk.Button(f_button, text='Stop', font=("",15), command=self.stop, state=tk.DISABLED)
        self.b_reset = tk.Button(f_button, text='Reset', font=("",15), command=self.reset, state=tk.DISABLED)
        self.b_start.pack(side=tk.LEFT,ipadx=30, padx=10)
        self.b_stop.pack(side=tk.LEFT,ipadx=30, padx=10)
        self.b_reset.pack(side=tk.LEFT,ipadx=30, padx=10)

    def time_init(self):
        self.time.set("セットする時間を秒単位で入力してください。")

    def time_err(self):
        self.time.set("不正な入力値です。")        

    def time_set(self):
        self.h = self.count // 3600
        self.m = (self.count % 3600) // 60
        self.s = (self.count % 3600) % 60        
        self.time.set("のこり %02d時間 %02d分 %02d秒" % (self.h,self.m,self.s))

    def start(self):
        try:
            if not self.count:
                self.count = int(self.entry.get())                                   
        except:
            self.time_err()
            return

        self.started = True
        self.time_set()
        if(0 < self.count <= 10):
            self.label.config(bg="red")
        self.after(1000, self.counting)
        self.entry.config(state=tk.DISABLED)
        self.b_start.config(state=tk.DISABLED)
        self.b_stop.config(state=tk.NORMAL)
        self.b_reset.config(state=tk.DISABLED) 
 
    def stop(self):
        self.started = False
        self.b_start.config(state=tk.NORMAL)
        self.b_stop.config(state=tk.DISABLED)
        self.b_reset.config(state=tk.NORMAL)
 
    def reset(self):
        self.count = None
        self.time_init()
        self.label.config(bg="white")
        self.b_reset.config(state=tk.DISABLED)
        self.entry.configure(state=tk.NORMAL)
 
    def counting(self):
        if self.started:
            self.count -=1
            self.time_set()

            if (0 < self.count <= 10):
                self.label.config(bg="red")

            if self.count <= 0:
                self.stop()
                self.reset()

            self.after(1000, self.counting)

if __name__ == '__main__':
    app = TimerApp()
    app.pack()
    app.mainloop()