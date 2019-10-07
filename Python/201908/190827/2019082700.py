import sys
import tkinter as tk
# ダイアログの使用
import tkinter.messagebox as tkm

root = tk.Tk()

# ウィンドウのタイトル設定
root.title(u"Python Test")

# ウィンドウのサイズ変更
root.geometry("400x300")

# ボタンが押されたら呼び出す関数
def deleteEntry(event):
    "Entryの中身をすべて削除"
    entry1.delete(0,tk.END)

def showMessage(text):
    tkm.showinfo("ダイアログのタイトル",text)

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

# Buttonを設置
#button1 = tk.Button(text=u"button1")
#button1 = tk.Button(text=u"Elase",width=50)
button1 = tk.Button(text=u"Message Button",width=50,command=lambda:showMessage(entry1.get()))

#button1.bind("<Button-1>",deleteEntry) # buttonが押されたときに実行される関数をバインド
button1.pack()

# 普通のダイアログ
#tkm.showinfo("ダイアログ00","普通のダイアログ")

# ワーニングなダイアログ
#tkm.showwarning("ダイアログ01","ワーニングのダイアログ")

# エラーな感じなダイアログ
#tkm.showerror("ダイアログ02","エラーな感じのダイアログ")

# YES/NOなダイアログ（YESがクリックされたら戻り値がtrue、NOならfalse）
#tkm.askyesno("ダイアログ03","YES/NOなダイアログ")

# リトライキャンセルダイアログ（リトライがクリックされたら戻り値がtrue、キャンセルならfalse）
#tkm.askretrycancel("ダイアログ04","リトライキャンセルダイアログ")

# OK/NOダイアログ（リトライがクリックされたら戻り値が'yes'、キャンセルなら'no'）
#tkm.askquestion("ダイアログ05","OK/NOダイアログ")

# OK/CANCELダイアログ（OKがクリックされたら戻り値がtrue、キャンセルならfalse
#tkm.askokcancel("ダイアログ06","OK/CANCELダイアログ")

# リストボックスを設置
listbox1 = tk.Listbox()
listbox1.pack()

root.mainloop()
