import tkinter as tk

class Application(tk.Frame):
    class Info(): # 計算途中の値を貯めておく「構造体」的用法の内部クラス
        def __init__(self,x):
            self.x = x  # 平方根を求めたい値
            self.i = 1  # 回数
            self.low, self.high = 0.0, max(1.0, x)
            
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()
        self.info = None

    def create_widgets(self):
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.btn = tk.Button(self, text='推定', command=self.estimate)
        self.btn.pack()
        self.result_label = tk.Label(self)
        self.result_label.pack()
    
    def estimate(self):
        s = self.entry.get()
        try:
            x = float(s)
        except:
            self.result_label.configure(text=f'{s}は不正な入力値です。',fg="red")
            return

        if self.info is None or self.info.x != x:
            self.info = self.Info(x)

        info = self.info

        ans = (info.high+info.low)/2.0
        if ans**2 < x:
            info.low = ans
        else:
            info.high = ans

        self.result_label.configure(text=f'{info.i}回目: {ans}',fg='black')
        info.i += 1


root = tk.Tk()
root.title('平方根の推定')
root.geometry('200x80')
app = Application(root)
app.mainloop()