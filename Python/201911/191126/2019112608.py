import tkinter as tk

def convert():
    src=entry.get()
    try:
        if val.get() == 0:
            result=eval("0b"+src)
        elif val.get() == 1:
            result=eval("0o"+src)
        else:
            result=eval("0x"+src)
        mess = f"変換結果は {result} です。"        
    except:
        mess="不正な形式です。"
    result_label.config(text=mess)

root = tk.Tk()
root.geometry("250x200")
root.title("〇進数→10進数変換")
tk.Label(root, text="チェックしている〇進数を入力してください").pack()

# ラジオボタンの設置
val = tk.IntVar()
val.set(0)

r0 = tk.Radiobutton(text = '2進数', variable = val, value = 0)
r0.pack()
r1 = tk.Radiobutton(text = '8進数', variable = val, value = 1)
r1.pack()
r2 = tk.Radiobutton(text = '16進数', variable = val, value = 2)
r2.pack()

entry=tk.Entry(root)
entry.pack()

btn=tk.Button(root,text="10進数に変換",command=convert)
btn.pack()

result_label = tk.Label(root,text="入力後にボタンを押してください")
result_label.pack()

root.mainloop()
