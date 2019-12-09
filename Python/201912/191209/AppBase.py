import tkinter as tk

class AppBase(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.__create_header_widgets()
        self.create_extra_widgets()
        self.__create_footer_widgets()
        self.pack(expand=True, fill=tk.BOTH)

    def __create_header_widgets(self):
        frame = tk.Frame(self)
        self._entry_sv = tk.StringVar(self)
        self._entry = tk.Entry(frame, font=('',16),
                               textvariable=self._entry_sv)
        self._entry.pack(side=tk.LEFT, expand=True,fill=tk.X)
        self._entry.bind('<Return>',self.__on_enter)
        self._enter_btn = tk.Button(frame, text='Enter', font=('',16),
                                    command=self.__on_enter)
        self._enter_btn.pack(side=tk.RIGHT)
        frame.pack(side=tk.TOP,fill=tk.X)

    def __create_footer_widgets(self):
        self._disp_sv = tk.StringVar(self)
        self._disp = tk.Label(self, font=('',16),
                              justify=tk.LEFT, anchor=tk.NW,
                              height=8,width=50,
                              textvariable=self._disp_sv)
        self._disp.pack(side=tk.BOTTOM, anchor='s', expand=1, fill=tk.BOTH,
                        ipadx=16)

    # 表示用
    def display(self, msg):
        self._disp_sv.set(msg)

    def __on_enter(self,event=None):
        self.on_enter(self._entry_sv)

    # 仮想メソッド
    def create_extra_widgets(self):
        pass

    # これも仮想メソッド
    def on_enter(self, sv):
        pass