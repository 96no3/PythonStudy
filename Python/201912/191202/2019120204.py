import tkinter.filedialog as FD

f = FD.askopenfile(mode='r', initialfile='yuri2.gif', 
                   initialdir='C:/flower',
                   filetypes =[('gif files', '*.gif'),
                               ('png files', '*.png'),
                               ("jpg files",('*.jpg', '*.jpeg'))])
"""
path = FD.askopenfilename(title="処理対象ファイルを指定してください",
                   initialfile='yuri2.gif', 
                   initialdir='C:/flower',
                   filetypes =[('gif files', '*.gif'),
                               ('png files', '*.png'),
                               ("jpg files",('*.jpg', '*.jpeg'))])

directory = FD.askdirectory(title="対象フォルダを指定してください",
                   initialdir='C:/flower')
"""
print(f) 