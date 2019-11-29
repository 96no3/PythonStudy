import tkinter as tk

class App(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master.title("2進数→10進数変換")
        self.master.geometry("250x100")
        self.create_widgets()        

    def create_widgets(self):
        tk.Label(self, text="2進数を入力してください").pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        btn=tk.Button(self,text="10進数に変換",command=self.convert)
        btn.pack()
        self.result_label = tk.Label(self,text="2進数を入力してボタンを押してください")
        self.result_label.pack()

    def convert(self):
        src=self.entry.get()
        try:
            self.result_label.config(text=f"変換結果は {eval('0b'+src)} です。")
        except:
            self.result_label.config(text="不正な形式です。")
            
if __name__ == '__main__':
    app = App()
    app.pack()
    app.mainloop()

