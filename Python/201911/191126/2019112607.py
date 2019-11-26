import tkinter as tk

root = tk.Tk()
root.geometry("250x100")
root.title("2進数→10進数変換")
tk.Label(root, text="2進数を入力してください").pack()

entry=tk.Entry(root)
entry.pack()

def convert():
    src=entry.get()
    try:
        result=eval("0b"+src)
        result_label.config(text=f"変換結果は {result} です。")
    except:
        result_label.config(text="不正な形式です。")

btn=tk.Button(root,text="10進数に変換",command=convert)
btn.pack()

result_label = tk.Label(root,text="2進数を入力してボタンを押してください")
result_label.pack()
    
root.mainloop() # モジュール化する場合は追加必須
