import tkinter
from tkinter import ttk
#2.Comboboxクラス
class TestCombobox(ttk.Combobox):
    def __init__(self, var, master=None):
        li = ['Easy', 'Normal', 'Hard']     #初期値
        super().__init__(master, values=li) #初期値の設定
        self.var = var                      #varをインスタンス変数化
        self.bind(                          #値選択時にshow_selectedを実行
            '<<ComboboxSelected>>',
            self.show_selected
            )
        
    def show_selected(self, event):
        self.var.set(self.get())    #選択した値をvarにセット
if __name__ == "__main__":
    root = tkinter.Tk()
    
    #1.変数の設定
    var = tkinter.StringVar(master=root)
    #3.ラベル、コンボボックスの生成
    l = tkinter.Label(textvariable=var)
    c = TestCombobox(master=root, var=var)
    l.pack()
    c.pack()
    root.mainloop()
