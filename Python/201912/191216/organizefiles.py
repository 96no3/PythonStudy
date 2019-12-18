import re
import os
import subprocess
import tkinter as Tk
import tkinter.filedialog as D
import tkinter.messagebox as M

FILE_TYPES= ['text', 'excel', 'slide', 'image', 'music', 'movie', 'compress', 'program']
TEXT_TYPES= ['doc', 'docx', 'odt', 'rtf', 'pdf', 'txt']
EXCEL_TYPES= ['xlsx', 'csv', 'tsv', 'xls']
SLIDE_TYPES= ['pptx', 'ppt', 'odp']
IMAGE_TYPES = ['gif', 'png', 'bmp', 'jpeg', 'jpg', 'tga', 'tif', 'ppm']
MUSIC_TYPES = ['mp3', 'wav', 'wma', 'asf', 'aac', 'flac', 'm4a']
MOVIE_TYPES = ['mp4', 'mpg', 'mpeg', 'wmv', 'avi', 'mkv']
COMPRESS_TYPES = ['zip', 'lzh', '7z', 'cab', 'tar', 'rar']
PROGRAM_TYPES = ['c', 'cpp', 'h', 'cs', 'py', 'js', 'bat', 'php', 'java']
GEO_MAIN = '750x400+20+20'

class Frame(Tk.Frame):

    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.master.title('Organize Files')
        self.master.geometry(GEO_MAIN)
        
        ### Menu
        menu_bar = Tk.Menu(self, tearoff=0)
        # File
        menu_file = Tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=menu_file,  underline=0)
        menu_file.add_command(label="Browse Dir.", command=self.browse, underline=0, accelerator = 'Ctrl-O')
        menu_file.add_command(label="ReLoad", command=self.load_dir, underline=0, accelerator = 'Ctrl-R')
        menu_file.add_command(label="Execution", command=self.execution, underline=0, accelerator = 'Ctrl-S')        
        menu_file_type = Tk.Menu(menu_file, tearoff=0)
        menu_file.add_cascade(label="File Type", menu=menu_file_type, underline=0)
        menu_file.add_separator()
        menu_file.add_command(label="Exit", command=self.exit, underline=0 , accelerator = 'Ctrl-Q')

        menu_text_type = Tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="text", menu=menu_text_type, underline=0)
        menu_excel_type = Tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="excel", menu=menu_excel_type, underline=0)
        menu_slide_type = Tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="slide", menu=menu_slide_type, underline=0)
        menu_image_type = Tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="image", menu=menu_image_type, underline=0)
        menu_music_type = Tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="music", menu=menu_music_type, underline=0)
        menu_movie_type = Tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="movie", menu=menu_movie_type, underline=0)
        menu_compress_type = Tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="compress", menu=menu_compress_type, underline=0)
        menu_program_type = Tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="program", menu=menu_program_type, underline=0)
        menu_bar.add_command(label="Help", command=self.show_info, underline=0)

        # short-cuts
        self.master.bind('<Control-KeyPress-o>', self.browse)
        self.master.bind('<Control-KeyPress-s>', self.execution)
        self.master.bind('<Control-KeyPress-r>', self.load_dir)
        self.master.bind('<Control-KeyPress-q>', self.exit) 
        
        # check buttons in menu_file_type
        self.var_type = dict()
        for i, file_type in enumerate(FILE_TYPES):
            self.var_type[file_type] = Tk.IntVar()
            menu_file_type.add_checkbutton(label=file_type, variable=self.var_type[file_type])
            menu_file_type.invoke(i)

        # check buttons in menu_text_type
        self.var_text_type = dict()
        for i, text_type in enumerate(TEXT_TYPES):
            self.var_text_type[text_type] = Tk.IntVar()
            menu_text_type.add_checkbutton(label=text_type, variable=self.var_text_type[text_type])
            menu_text_type.invoke(i)

        # check buttons in menu_excel_type
        self.var_excel_type = dict()
        for i, excel_type in enumerate(EXCEL_TYPES):
            self.var_excel_type[excel_type] = Tk.IntVar()
            menu_excel_type.add_checkbutton(label=excel_type, variable=self.var_excel_type[excel_type])
            menu_excel_type.invoke(i)

        # check buttons in menu_slide_type
        self.var_slide_type = dict()
        for i, slide_type in enumerate(SLIDE_TYPES):
            self.var_slide_type[slide_type] = Tk.IntVar()
            menu_slide_type.add_checkbutton(label=slide_type, variable=self.var_slide_type[slide_type])
            menu_slide_type.invoke(i)

        # check buttons in menu_image_type
        self.var_image_type = dict()
        for i, image_type in enumerate(IMAGE_TYPES):
            self.var_image_type[image_type] = Tk.IntVar()
            menu_image_type.add_checkbutton(label=image_type, variable=self.var_image_type[image_type])
            menu_image_type.invoke(i)

        # check buttons in menu_music_type
        self.var_music_type = dict()
        for i, music_type in enumerate(MUSIC_TYPES):
            self.var_music_type[music_type] = Tk.IntVar()
            menu_music_type.add_checkbutton(label=music_type, variable=self.var_music_type[music_type])
            menu_music_type.invoke(i)

        # check buttons in menu_movie_type
        self.var_movie_type = dict()
        for i, movie_type in enumerate(MOVIE_TYPES):
            self.var_movie_type[movie_type] = Tk.IntVar()
            menu_movie_type.add_checkbutton(label=movie_type, variable=self.var_movie_type[movie_type])
            menu_movie_type.invoke(i)

        # check buttons in menu_compress_type
        self.var_compress_type = dict()
        for i, compress_type in enumerate(COMPRESS_TYPES):
            self.var_compress_type[compress_type] = Tk.IntVar()
            menu_compress_type.add_checkbutton(label=compress_type, variable=self.var_compress_type[compress_type])
            menu_compress_type.invoke(i)

        # check buttons in menu_program_type
        self.var_program_type = dict()
        for i, program_type in enumerate(PROGRAM_TYPES):
            self.var_program_type[program_type] = Tk.IntVar()
            menu_program_type.add_checkbutton(label=program_type, variable=self.var_program_type[program_type])
            menu_program_type.invoke(i) 

        # add menu bar
        try:
            self.master.config(menu=menu_bar)     # this required to show the menu bar
        except AttributeError:
            self.master.Tk.call(master, "config", "-menu", menu_bar)

        self.create_widgets()
        self.pack(fill=Tk.BOTH, expand=1)

    def create_widgets(self):
        f=Tk.Frame(self)
        f.pack(fill=Tk.X)
        f_dir = Tk.LabelFrame(f, text='Directory')
        f_dir.pack(side=Tk.LEFT, padx=10, pady=2)
        self.e_dir = Tk.Entry(f_dir, width=70)
        self.e_dir.pack(side=Tk.LEFT)
        self.e_dir.bind('<Return>', self.load_dir)
        self.b_dir = Tk.Button(f_dir, text='Browse', command=self.browse)
        self.b_dir.pack(side=Tk.LEFT, padx=2)        
        b_info=Tk.Button(f, bitmap='info', width=25, command=self.show_info)
        b_info.pack(side=Tk.LEFT, padx=20, pady=10)        
        
        f_type = Tk.LabelFrame(self, text='File Type')
        f_type.pack(anchor=Tk.W,padx=10, pady=2)
        self.e_type = Tk.Entry(f_type, width=10)
        self.e_type.pack(side=Tk.LEFT)
        self.e_type.bind('<Return>', self.load_dir)
        self.b_re = Tk.Button(f_type, text='ReLoad', command=self.load_dir)
        self.b_re.pack(side=Tk.LEFT, padx=2)    
        for file_type in FILE_TYPES:
            cb = Tk.Checkbutton(f_type, text=file_type, variable=self.var_type[file_type],
                                relief=Tk.FLAT, justify = Tk.LEFT)
            cb.pack(side=Tk.LEFT, padx=5)  
          

        f_folder = Tk.LabelFrame(self, text='New folder name')
        f_folder.pack(anchor=Tk.W, padx=10, pady=2)
        self.e_folder = Tk.Entry(f_folder, width=30)
        self.e_folder.pack(side=Tk.LEFT)
        self.e_folder.bind('<Return>', self.execution)
        self.b_folder = Tk.Button(f_folder, text='Execution', command=self.execution)
        self.b_folder.pack(side=Tk.LEFT, padx=2)

        f_list = Tk.LabelFrame(self, text='Files list')
        f_list.pack(side=Tk.LEFT, anchor=Tk.NW, padx=10, pady=2)
        self.once = False
        self.listbox = Tk.Listbox(f_list,selectmode=Tk.EXTENDED)
        self.listbox.pack(side=Tk.LEFT, fill=Tk.Y, expand=1)
        self.listbox.bind("<3>", self.pick_up)         
        self.scrollbar = Tk.Scrollbar(f_list, orient=Tk.VERTICAL,command=self.listbox.yview)
        self.listbox['yscrollcommand'] = self.scrollbar.set
        self.scrollbar.pack(side=Tk.RIGHT, fill=Tk.Y, expand=1)
        self.b_pick = Tk.Button(f_list, text='Pick up', command=self.pick_up)
        self.b_pick.pack(side=Tk.BOTTOM,padx=2)    

        f_pick = Tk.LabelFrame(self, text='Pick up')
        f_pick.pack(side=Tk.LEFT, anchor=Tk.NW, padx=10, pady=2)
        self.pickups=[]
        self.listbox2 = Tk.Listbox(f_pick,selectmode=Tk.EXTENDED)
        self.listbox2.pack(side=Tk.LEFT, fill=Tk.Y, expand=1)
        self.listbox2.bind("<3>", self.remove)       
        self.scrollbar2 = Tk.Scrollbar(f_pick, orient=Tk.VERTICAL,command=self.listbox2.yview)
        self.listbox2['yscrollcommand'] = self.scrollbar2.set
        self.scrollbar2.pack(side=Tk.RIGHT, fill=Tk.Y, expand=1)        
        self.b_pick = Tk.Button(f_pick, text='Remove', command=self.remove)
        self.b_pick.pack(side=Tk.BOTTOM,padx=2)

    ## functions ------------------------------------------------
    def make_regexp(self,types):        
        self.make_compile_list(types)
        string = "\.("
        for k in self.compiles:
            string += k + '|'
        string = string[0:-1] + ')$'
        return re.compile(string, re.I)

    def make_compile_list(self,types):
        self.compiles=[]
        self.compiles.append(self.e_type.get())
        for k, v in types.items():
            if v.get():
                if k == "text":
                    self.add_compile_list(self.var_text_type)
                elif k == "excel":
                    self.add_compile_list(self.var_excel_type)
                elif k == "slide":
                    self.add_compile_list(self.var_slide_type)
                elif k == "image":
                    self.add_compile_list(self.var_image_type)
                elif k == "music":
                    self.add_compile_list(self.var_music_type)
                elif k == "movie":
                    self.add_compile_list(self.var_movie_type)
                elif k == "compress":
                    self.add_compile_list(self.var_compress_type)
                elif k == "program":
                    self.add_compile_list(self.var_program_type)
    
    def add_compile_list(self,types):
        for k, v in types.items():
            if v.get():
                self.compiles.append(k)

    def update(self, dir_path, types):
        if self.once:
            self.listbox.delete(0, Tk.END)
            self.renew()

        self.once=True
        pat = self.make_regexp(types)
        os.chdir(dir_path)
        self.file_list=[]
        for f in os.listdir():
            if pat.search(f):
                self.file_list.append(f)
        self.listbox.insert(Tk.END, *self.file_list)                

    def browse(self, event=None):
        dir_path = D.askdirectory()
        if dir_path:
            self.e_dir.delete(0, Tk.END)
            self.e_dir.insert(0, dir_path)
            subprocess.Popen(['explorer', dir_path.replace("/", "\\")])            
            self.load_dir()

    def load_dir(self, event=None):
        self.update(self.e_dir.get(), self.var_type)

    def renew(self):
        if self.pickups:
            self.pickups.clear()
            self.listbox2.delete(0, Tk.END)        

    def pick_up(self, event=None):
        self.renew()
        selected = [ int(x) for x in self.listbox.curselection()]
        if len(selected) == 0:
            return None

        for i in selected:
            self.pickups.append(self.file_list[i])
            self.listbox2.insert(Tk.END,self.file_list[i])
        self.listbox.selection_clear(min(selected), max(selected))

    def remove(self, event=None):
        if not self.pickups:
            return None

        selected2 = [ int(x) for x in self.listbox2.curselection()]
        if len(selected2) == 0:
            return None
        elif len(selected2) > 1:
            M.showwarning(u"警告",
                          u"削除の複数選択には対応しておりません。\n"
                          u"1つずつ選択してRemoveしてください。")
            return None
        
        for i in selected2:
            self.pickups.remove(self.pickups[i])
            self.listbox2.delete(i)
        self.listbox2.selection_clear(min(selected2), max(selected2))

    def execution(self,event=None):
        if not self.pickups:
            M.showerror(u"注意",
                        u"ファイルを選択してください。")
            return None

        name = self.e_folder.get()
        if name:
            m = M.askokcancel(u"確認",
                            u"選択したファイルをフォルダにまとめて良いですか？")
            if m:
                for file in self.pickups:
                    os.renames(file,name+"\\"+file)
                M.showinfo("完了","フォルダ分けしました。")
                self.renew()
                self.e_folder.delete(0,Tk.END)
            else:
                return None
        else:
            M.showerror(u"注意",
                        u"フォルダ名を入力してください。")

    def exit(self,event=None):
        self.master.destroy()

    def show_info(self):
        M.showinfo(u"<使い方>",
                   u"Entry か Browseボタンでディレクトリを選択してください。\n"
                   u"そのディレクトリに含まれるファイルの一覧が表示されます。\n"
                   u"別窓でディレクトリが展開されます。\n"
                   u"一覧に表示するファイルの種類をメニューバーのチェックボタンで変えることができます。\n\n"
                   u"～～ファイル整理の方法～～\n"
                   u"リストボックスからファイルをマウス左ボタンで選択してください。\n"
                   u"マウス左ボタンのドラッグ、Shift + マウス左ボタン、Ctrl + マウス左ボタン などで複数の選択が可能です。\n"
                   u"選択が終わったら、マウス右ボタンまたはPick upボタンをクリックしてください。\n" 
                   u"選択されたファイルが右側に表示されます。\n"
                   u"New folder nameを入力してEnterまたはExecutionを押してください。\n"
                   u"確認ダイアログでOKを押すと、選択したファイルをまとめたフォルダが作成されます。")

##------------------------------------------------ 
if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()