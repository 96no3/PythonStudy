# ファイル選択ダイアログ
import tkinter.filedialog as fd

# ファイル選択ダイアログを表示 戻り値はファイルのフルパス
path = fd.askopenfilename(
    title = "処理対象ファイルを指定してください", # ダイアログ上部のタイトル設定
    filetypes = [("Python",".py"),("PNG",".png")]) # タプルで指定した形式のファイルだけを表示

print(path)
