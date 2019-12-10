from AppBase import *
from tkinter import font
import math,pylab,random

"""
xs=[*range(1,101)]
moment(xs,1) # 平均値
moment(xs,2,moment(xs,1)) # 分散
# 積率による分散の計算
moment(xs,2) - moment(xs,1)**2
"""

class Application(AppBase):
    def __init__(self, master=None):
        super().__init__(master)
        self.bind_all('<Delete>', self.reset)
        self.bind_all('<s>', self.show)
        self.bind_all('<g>', self.gauss)
        self.bind_all('<p>', self.plot)
        self._xs = []
    
    @staticmethod
    def moment(xs,m,u=0):
        return sum((x-u)**m for x in xs) / len(xs)

    def create_extra_widgets(self):
        f_table = tk.Frame(self)
        f_table.pack(expand=1, fill=tk.BOTH)
        self._tsv = tk.StringVar()        
        self._table = tk.Label(f_table,justify=tk.LEFT, anchor=tk.NW, textvariable=self._tsv)
        self._table.pack(expand=1, fill=tk.BOTH)
        f_result = tk.Frame(self,relief=tk.RIDGE, bd=4)
        f_result.pack(expand=1, fill=tk.BOTH)
        font1 = font.Font(family='Helvetica', size=15, weight='bold')
        self._a = tk.StringVar()
        self._ave = tk.Label(f_result, font=font1,justify=tk.LEFT, anchor=tk.NW, textvariable=self._a)
        self._ave.pack(side=tk.LEFT)
        self._b = tk.StringVar()
        self._var = tk.Label(f_result, font=font1,justify=tk.LEFT, anchor=tk.NW, textvariable=self._b)
        self._var.pack(side=tk.LEFT)
        self._c = tk.StringVar()
        self._dev = tk.Label(f_result, font=font1,justify=tk.LEFT, anchor=tk.NW, textvariable=self._c)
        self._dev.pack(side=tk.LEFT)
        self.init_table()

    def init_table(self):
        self._tsv.set("値を入力してEnterを押してください")
        self._a.set("")
        self._b.set("")
        self._c.set("")

    def set_table(self):
        self._tsv.set(" | ".join(f"{i+1}番目:{x}" for i,x in enumerate(self._xs)))

    def set_ave(self):
        self.mu = Application.moment(self._xs,1)
        self._a.set("平均値:%.4f" % self.mu)

    def set_var(self):
        self.sigma2 = Application.moment(self._xs,2,Application.moment(self._xs,1))
        self._b.set("分散:%.4f" % self.sigma2)

    def set_dev(self):
        self.sigma = math.sqrt(self.sigma2)
        self._c.set("標準偏差:%.4f" % self.sigma)

    def reset(self,event=None):
        self._xs.clear()
        self.init_table()
        self.display('')

    def on_enter(self, sv):
        s = sv.get()
        try:
            x = float(s)
            self.display(f'整数値の取得に成功しました\n--> {x}')
            self._xs.append(x)
            self.set_table()
            self.set_ave()            
            self.set_var()
            self.set_dev()          
            sv.set('')
        except:
            self.display(f'数値に変換できません! {s}')

    def show(self,event=None):
        pylab.hist(self._xs)
        pylab.show()

    def gauss(self,event=None):
        pylab.hist([random.gauss(self.mu,self.sigma) for _ in range(10000)],bins=50)
        pylab.show()

    def plot(self,event=None):
        xs=[x/100 for x in range(-400,401)]
        ys=[(1/2*math.pi*self.sigma2)*math.exp(-(x-self.mu)**2/2*self.sigma2) for x in xs]
        pylab.plot(xs,ys)
        pylab.show()

if __name__ == '__main__':
    app = Application()
    app.mainloop()
