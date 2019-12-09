from AppBase import *
from tkinter import font
import math

class Application2(AppBase):
    def __init__(self, master=None):
        super().__init__(master)
        self.bind_all('<Delete>', self.reset)
        self.sum = 0
        self.sum2 = 0
        self.n = 0

    def create_extra_widgets(self):
        f_table = tk.Frame(self)
        f_table.pack(expand=1, fill=tk.BOTH)
        self._nsv = tk.StringVar()        
        self.l_n = tk.Label(f_table,justify=tk.LEFT, anchor=tk.NW, textvariable=self._nsv)
        self.l_n.pack(side=tk.LEFT)
        self._ssv = tk.StringVar()  
        self.l_s = tk.Label(f_table,justify=tk.LEFT, anchor=tk.NW, textvariable=self._ssv)
        self.l_s.pack(side=tk.LEFT)
        self._s2sv = tk.StringVar()
        self.l_s2 = tk.Label(f_table,justify=tk.LEFT, anchor=tk.NW, textvariable=self._s2sv)
        self.l_s2.pack(side=tk.LEFT)    
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

    def init_value(self):
        self._a.set("")
        self._b.set("")
        self._c.set("")

    def set_value(self):
        ave = self.sum / self.n
        var = self.sum2 / self.n - ave**2
        self._a.set("平均値:%.4f" % ave)
        self._b.set("分散:%.4f" % var)
        self._c.set("標準偏差:%.4f" % math.sqrt(var))
        self._nsv.set(f"{self.n}回目")
        self._ssv.set(f"合計:{self.sum}")
        self._s2sv.set(f"二乗合計:{self.sum2}")

    def reset(self,event=None):
        self.init_value()
        self.display('')

    def on_enter(self, sv):
        s = sv.get()
        try:
            x = float(s)
            self.display(f'整数値の取得に成功しました\n--> {x}')
            self.sum += x
            self.sum2 += x**2
            self.n += 1
            self.set_value()
            sv.set('')
        except:
            self.display(f'数値に変換できません! {s}')

if __name__ == '__main__':
    app = Application2()
    app.mainloop() 
