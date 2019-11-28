import tkinter as tk

root = tk.Tk()
# gridで配置
tk.Button(root,text="B-00",bg="#aa1a00").grid(row=0,column=0)
tk.Button(root,text="B-01",bg="#9a2a00").grid(row=0,column=1)
tk.Button(root,text="B-02",bg="#8a3a00").grid(row=0,column=2)
tk.Button(root,text="B-03",bg="#7a4a00").grid(row=1,column=0,columnspan=3,sticky=tk.W + tk.E)
tk.Button(root,text="B-04",bg="#6a5a00").grid(row=0,column=3,rowspan=2,sticky=tk.N + tk.S)
tk.Button(root,text="B-05",bg="#5a6a00").grid(row=2,column=0,columnspan=2,sticky=tk.W + tk.E)
tk.Button(root,text="B-06",bg="#4a7a00").grid(row=2,column=2,columnspan=2,sticky=tk.W + tk.E)
tk.Button(root,text="B-07",bg="#3a8a00").grid(row=1,column=4,rowspan=2,sticky=tk.N+tk.S)

