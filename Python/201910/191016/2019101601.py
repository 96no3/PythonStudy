# ダイアログを使ったGUI
import tkinter.messagebox as mb

# ダイアログ表示（「Yes」「No」でTrue or Falseを返す）
ans = mb.askyesno("質問","ラーメンは好きですか？")
if ans == True:
    # OKボタンだけのダイアログ表示
    mb.showinfo("同意","僕も好きです")
else:
    mb.showinfo("本当？","まさか、ラーメンが嫌いだなんて！")

# 他のダイアログメソッド
"""
# 「OK」「Cancel」でTrue or Falseを返す
mb.askokcancel("タイトル","メッセージ”)

# 「Retry」「Cancel」でTrue or Falseを返す
mb.askretrycancel("タイトル","メッセージ”)

# OKボタンを持つエラーダイアログ
mb.showerror("タイトル","メッセージ”)

# OKボタンを持つ警告ダイアログ
mb.showwarning("タイトル","メッセージ”)
"""

