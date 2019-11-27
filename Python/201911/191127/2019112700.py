import tkinter as tk
#from tkinter import messagebox as mb # ダイアログ表示のサブモジュール
import tkinter.messagebox as mb # インポートの方法2
import tkinter.filedialog as fdlg # ファイルダイアログ表示のサブモジュール

root = tk.Tk()
tk.Button(root,text="0").pack(fill=tk.X) # オプションfillを指定 tk.Xで枠x幅
# フレーム作成
frame1 = tk.Frame(root,bg="blue")
tk.Button(frame1,text="1").pack(side="left")
tk.Button(frame1,text="2").pack(side="left")
frame1.pack(side="left",fill=tk.Y) # tk.Yで枠y幅

frame2 = tk.LabelFrame(root,text="xxxx") # ラベル付きフレーム
tk.Button(frame2,text="3").pack(side="right")
tk.Button(frame2,text="4").pack(side="right")
frame2.config(bg="green",fg="lightgreen") # ラベルのオプション
frame2.pack(side="right",fill=tk.Y)

tk.Button(root,text="5").pack(side="bottom")
tk.Button(root,text="6").pack(side="bottom")
w = tk.Button(root,text="7")
w.pack()
# w.master
# w.master is root
# w.master is frame1
# w.children

# Buttonのオプションをテストする関数
def test(**kwds):
    root = tk.Tk()
    root.config(bg="white")
    tk.Button(text="Button",bg="yellow").pack(**kwds)
    root.mainloop()

#test()
#test(fill=tk.X)
#test(fill=tk.Y,side="left")
#test(fill=tk.BOTH,expand=1)
#test(fill=tk.BOTH,expand=1,padx=50)
#test(fill=tk.BOTH,expand=1,pady=50)
#test(fill=tk.BOTH,expand=1,padx=50,pady=50)
#test(ipadx=100,ipady=50)
