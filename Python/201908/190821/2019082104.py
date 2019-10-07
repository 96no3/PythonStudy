import sys
import tkinter as tk

root = tk.Tk()

# ウィンドウのタイトル設定
root.title(u"Python Test")

# ウィンドウのサイズ変更
root.geometry("400x300")

# ラベル
#static1 = tk.Label(text=u"test")
static1 = tk.Label(text=u"▼Entry▼",foreground="#ff0000",background="#000000")

static1.pack()
#static1.place(x=0,y=150)

# Entry出現
#Entry1 = tk.Entry()
entry1 = tk.Entry(width=50) # widthプロパティで大きさを変える
entry1.insert(tk.END,u"挿入する文字列") # 最初から文字を入れておく
entry1.pack()

# Entryの値を取得
entry1Value = entry1.get()
print(entry1Value)

# Entryの値を削除
entry1.delete(0,tk.END) # Entryの中身を0文字目から最後の文字まで削除

# Buttonを設置してみる
#button1 = tk.Button(text=u"button1")
button1 = tk.Button(text=u"button1",width=50)
button1.pack()

root.mainloop()