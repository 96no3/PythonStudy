import tkinter as tk
"""
# 二分法での平方根計算
def my_sqrt(x,n=10):
    low,high = 0.0,max(1.0,x)
    for i in range(1,n+1):
        ans=(high+low)/2.0
        print(f"{i}回目の推定値: {ans}")
        if ans**2 < x:
            low = ans
        else:
            high = ans
    return ans

# ニュートン・ラフソン法での平方根計算
def my_sqrt2(x,n=10):
    ans = 1.0
    for i in range(1,n+1):
        ans = ans - (ans**2-x)/(2*ans)
        print(f"{i}回目の推定値: {ans}")
    return ans
"""    

class App(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master.title("平方根の推定値計算機")
        self.master.geometry("350x180")
        self.i = 1   # 処理回数
        self.pre = 0 # エントリーの値（比較用）
        self.low = 0 # 二分法での計算用数1
        self.max = 1 # 二分法での計算用数2 かつ ニュートン法での計算用数
        self.create_widgets()      

    def create_widgets(self):
        tk.Label(self, text="平方根の推定").pack()        
        
        f1=tk.Frame(self)
        f1.pack()
        # ラジオボタンの設置
        self.val = tk.IntVar()
        self.val.set(0)
        tk.Radiobutton(f1,text = '二分法', variable = self.val, value = 0).pack(side="left")        
        tk.Radiobutton(f1,text = 'ニュートン法', variable = self.val, value = 1).pack(side="left")        
        
        f2=tk.Frame(self)
        f2.pack()
        tk.Label(f2,text="表示桁数").grid(row=0,column=0)
        self.e1 = tk.Entry(f2)
        self.e1.insert(tk.END,"5")
        self.e1.grid(row=1,column=0,padx=5,)
        tk.Label(f2,text="平方根の数").grid(row=0,column=1)
        self.e2 = tk.Entry(f2)
        self.e2.grid(row=1,column=1,padx=5)

        btn=tk.Button(self,text="推定",command=self.echo)
        btn.pack(ipadx=50,pady=10)
        self.result_label = tk.Label(self,text="正の数を入力して、ボタンを押してください")
        self.result_label.pack()

    def echo(self):
        if self.val.get() == 0:
            func = self.my_sqrt
        else:
            func = self.my_sqrt2
        return func()

    def my_sqrt(self):        
        try:        
            v=int(self.e1.get())
            x=float(self.e2.get())
            if v>0 and x>0:
                if x == self.pre:
                    self.i += 1
                else:
                    self.pre = x
                    self.i = 1
                    self.low,self.high = 0.0,max(1.0,x)
                ans=(self.high+self.low)/2.0
                mess = f"{self.i}"+"回目の推定値: %.*f"%(v,ans)
                if ans**2 < x:
                    self.low = ans
                else:
                    self.high = ans

            elif v<0 or x<0:
                mess = "不正な形式です。"        
        except:
            mess = "不正な形式です。"
        
        self.result_label.config(text=mess)

    def my_sqrt2(self):        
        try:        
            v=int(self.e1.get())
            x=float(self.e2.get())
            if v>0 and x>0:
                if x == self.pre:
                    self.i += 1
                else:
                    self.pre = x
                    self.i = 1
                    self.max = 1
                self.max = self.max - (self.max**2-x) / (2*self.max)
                mess = f"{self.i}"+"回目の推定値: %.*f"%(v,self.max)

            elif v<0 or x<0:
                mess = "不正な形式です。"        
        except:
            mess = "不正な形式です。"
        
        self.result_label.config(text=mess)

if __name__ == '__main__':
    app = App()
    app.pack()
    app.mainloop()
