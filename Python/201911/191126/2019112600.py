import tkinter as tk
#from tkinter import messagebox as mb # ダイアログ表示のサブモジュール
import tkinter.messagebox as mb # インポートの方法2
import tkinter.filedialog as fdlg # ファイルダイアログ表示のサブモジュール

root = tk.Tk()
root.title("tkinter sample") # ウィンドウタイトルの設定

# ラベルの配置
label1 = tk.Label(root,text="This is a sample text")
label1.pack()
label2 = tk.Label(root,text="Label-2")
label2.pack()
label3 = tk.Label(root,text="Label-3")
label3.pack(side="left")
tk.Label(root,text="Label-4").pack(side="left")
tk.Label(root,text="Label-5").pack(side="bottom")
tk.Label(root,text="Label-6").pack(side="top")

# エントリーの配置
entry = tk.Entry(root)
entry.pack()
entry.get() # entryの値を取得

# ボタンの配置
b=tk.Button(root,text="press it!")
b.pack()

# 設定の変更
label2.config(bg="pink") # 背景色の設定
label2.config(fg="red") # 文字色の設定
label3.config(fg="white",bg="black")
label2.config(text="New Text")
label7=tk.Label(root,text="Label-7",bg="green")
label7.pack()

# エントリーに事前に値を挿入
entry.insert(0,"String")
entry.insert(0,"-----")

# ボタンを押したときの処理を設定
#b.config(command= lambda :print("PRESSED!"))
#b.config(command= lambda :print("Entry:",entry.get()))
b.config(command= lambda :label3.config(text=entry.get()))

# ウィンドウの大きさ変更
#root.geometry("500x400")
#root.geometry("+100+500") # 配置位置の指定
root.geometry("400x300+100+500")

# ダイアログの表示
mb.showinfo("info","message")
mb.showerror("info","message")
mb.askyesno("info","終了しますか？")
mb.askokcancel("info","終了しますか？")

# ファイルダイアログの表示
fdlg.askdirectory() # ファイルのディレクトリパスを返す
fdlg.askopenfilename() # 開くファイルの名前をディレクトリパスを含めて返す
fdlg.asksaveasfile() # ファイルの保存確認
