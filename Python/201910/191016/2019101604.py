# 文字数カウンタ
from tkinter import *

# テキストの文字数を数える関数
def count_text(event):
    s=main_text.get(1.0,END) # テキストの最初から最後まで取得
    info_label.config(text="{0}文字".format(len(s)))

# メインウィンドウを作成
root = Tk()
root.title("テキストカウンタ")

# テキストボックスを作成
main_text = Text(root)
main_text.bind("<Key>",count_text) # イベントを設定
main_text.pack()

# 文字数を表示するラベルを作成
info_label=Label(root)
info_label.pack()

# メインループ
root.mainloop()
