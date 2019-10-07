import sys
import tkinter as tk
# ダイアログの使用
import tkinter.messagebox as tkm
import random

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
    "Entryの中身をダイアログに表示"
    tkm.showinfo("ダイアログのタイトル",text)

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

def addList(text):
    "リストボックスに、Entryの中身を追加"
    listbox1.insert(tk.END,text)

def deleteSelectedList():
    "ボタンが押されたらリストボックスの選択されている部分を削除"
    # 選択されているリストの番号
    selectedIndex = tk.ACTIVE

    # それを削除
    listbox1.delete(selectedIndex)

def draw(event):
    # 「描く」ボタンが押されたら四角形で塗りつぶす
    canvas.create_rectangle(random.randint(0,300),random.randint(0, 200),\
                            random.randint(0, 400), random.randint(0, 250),\
                            tag="rectangle", fill='green', outline='#00f')

def erase(event):
    #「消す」ボタンが押されたら四角形を削除
    canvas.delete("rectangle")
    

"""
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

# 関数に引数を渡す場合は、commandオプションとlambda式を使う
#button1 = tk.Button(text=u"Message Button",width=50,command=lambda:showMessage(entry1.get()))
button1 = tk.Button(text=u"追加するButton",width=50,command=lambda:addList(entry1.get()))

#button1.bind("<Button-1>",deleteEntry) # buttonが押されたときに実行される関数をバインド
button1.pack()

button2 = tk.Button(text=u"削除するButton",width=50,command=lambda:deleteSelectedList())
button2.pack()


# リストボックスを設置
#listbox1 = tk.Listbox()
listbox1 = tk.Listbox(width=55,height=14)
listbox1.pack()
"""

# キャンバスエリア
canvas = tk.Canvas(root,width=400,height=250)
#canvas.create_rectangle(5,5,20,20,fill='green') # 四角形で塗りつぶし
#canvas.create_rectangle(5,5,20,20,fill='green',outline="#00f") # 枠線の色を変える
canvas.place(x=0,y=0)       # キャンバスエリアを(0,0)で指定

# 「描く」ボタン
button_draw = tk.Button(root,text=u"描く",width=15)
button_draw.bind("<Button-1>",draw)
button_draw.place(x=50,y=260)

# 「消す」ボタン
button_draw = tk.Button(root,text=u"消す",width=15)
button_draw.bind("<Button-1>",erase)
button_draw.place(x=200,y=260)

root.mainloop()