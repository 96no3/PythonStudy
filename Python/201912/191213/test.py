import os
import subprocess
import tkinter.filedialog as fd

# ファイル選択ダイアログを表示 戻り値はファイルのフルパス
file_path = fd.askopenfilename(
    title = "処理対象ファイルを指定してください", # ダイアログ上部のタイトル設定
    )
subprocess.Popen(['start', file_path], shell=True)


dir_path = fd.askdirectory()
subprocess.Popen(['explorer', dir_path.replace("/", "\\")])
#subprocess.run('explorer {}'.format(dir_path.replace("/", "\\")))

os.chdir(dir_path)
files = os.listdir()
name = "test"
for file in files:
   os.renames(file,name+"\\"+file)