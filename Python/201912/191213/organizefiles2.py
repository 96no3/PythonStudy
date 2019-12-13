import re
import os
import subprocess
import os.path as P
import tkinter as Tk
import tkinter.scrolledtext as S
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
GEO_MAIN = '680x600+20+20'
GEO_SATE = '+750+50'

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
 
        menu_text_type = Tk.Menu(menu_file, tearoff=0)
        menu_bar.add_command(label="text", command=menu_text_type, underline=0)
        menu_excel_type = Tk.Menu(menu_file, tearoff=0)
        menu_bar.add_command(label="excel", command=menu_excel_type, underline=0)
        menu_slide_type = Tk.Menu(menu_file, tearoff=0)
        menu_bar.add_command(label="slide", command=menu_slide_type, underline=0)
        menu_image_type = Tk.Menu(menu_file, tearoff=0)
        menu_bar.add_command(label="image", command=menu_image_type, underline=0)
        menu_music_type = Tk.Menu(menu_file, tearoff=0)
        menu_bar.add_command(label="music", command=menu_music_type, underline=0)
        menu_movie_type = Tk.Menu(menu_file, tearoff=0)
        menu_bar.add_command(label="movie", command=menu_movie_type, underline=0)
        menu_compress_type = Tk.Menu(menu_file, tearoff=0)
        menu_bar.add_command(label="compress", command=menu_compress_type, underline=0)
        menu_program_type = Tk.Menu(menu_file, tearoff=0)
        menu_bar.add_command(label="program", command=menu_program_type, underline=0)
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
        f_dir = Tk.LabelFrame(self, text='Directory')
        f_dir.pack(anchor=Tk.W, padx=10, pady=2)
        self.e_dir = Tk.Entry(f_dir, width=50)
        self.e_dir.pack(side=Tk.LEFT)
        self.e_dir.bind('<Return>', self.show_sum)
        self.b_dir = Tk.Button(f_dir, text='Browse', command=self.browse)
        self.b_dir.pack(side=Tk.LEFT, padx=2)
        f=Tk.Frame(self)
        f.pack(fill=Tk.X)
        b_info=Tk.Button(f, bitmap='info', width=25, command=self.show_info)
        b_info.pack(side=Tk.RIGHT, padx=20, pady=10, anchor=Tk.CENTER)        
        
        f_type = Tk.LabelFrame(f, text='File Type')
        f_type.pack(side=Tk.LEFT, padx=10, pady=2)
        self.e_type = Tk.Entry(f_type, width=10)
        self.e_type.pack(side=Tk.LEFT)
        self.e_type.bind('<Return>', self.add_type)
        for file_type in FILE_TYPES:
            cb = Tk.Checkbutton(f_type, text=file_type, variable=self.var_type[file_type],
                                relief=Tk.FLAT, justify = Tk.LEFT)
            cb.pack(side=Tk.LEFT, padx=5)  
        self.b_re = Tk.Button(f_type, text='ReLoad', command=self.load_dir)
        self.b_re.pack(side=Tk.LEFT, padx=2)      

        f_folder = Tk.LabelFrame(self, text='New folder name')
        f_folder.pack(anchor=Tk.W, padx=10, pady=2)
        self.e_folder = Tk.Entry(f_folder, width=30)
        self.e_folder.pack(side=Tk.LEFT)
        self.e_folder.bind('<Return>', self.execution)
        self.b_folder = Tk.Button(f_folder, text='Execution', command=self.execution)
        self.b_folder.pack(side=Tk.LEFT, padx=2)

        f_list = Tk.LabelFrame(self, text='Files list')
        f_list.pack(anchor=Tk.W, padx=10, pady=2)
        self.once = False
        self.stxt1 = S.ScrolledText(f_list, bg=self.cget('bg'), cursor=self.cget('cursor'), state=Tk.DISABLED)
        self.stxt1.pack(fill=Tk.BOTH, expand=1)

        f_pick = Tk.LabelFrame(self, text='Pick up')
        f_pick.pack(anchor=Tk.W, padx=10, pady=2)
        self.stxt2 = S.ScrolledText(f_pick, bg=self.cget('bg'), cursor=self.cget('cursor'), state=Tk.DISABLED)
        self.stxt2.pack(fill=Tk.BOTH, expand=1)
        self.b_pick = Tk.Button(self, text='Pick up', command=self.pick_up)
        self.b_pick.pack(padx=2)

    def make_regexp(self,types):
        string = "\.("
        for k, v in types.items():
            if v.get():
                if k == "text":
                    self.make_regexp(self.var_text_type)
                elif k == "excel":
                    self.make_regexp(self.var_excel_type)
                elif k == "slide":
                    self.make_regexp(self.var_slide_type)
                elif k == "image":
                    self.make_regexp(self.var_image_type)
                elif k == "music":
                    self.make_regexp(self.var_music_type)
                elif k == "movie":
                    self.make_regexp(self.var_movie_type)
                elif k == "compress":
                    self.make_regexp(self.var_compress_type)
                elif k == "program":
                    self.make_regexp(self.var_program_type)
                else:
                    string += k + '|'

        string = string[0:-1] + ')$'
        return re.compile(string, re.I)

    def update(self, dir_path, types):
        self.stxt.configure(state=Tk.NORMAL)
        if self.once:
            self.stxt.delete('1.0', Tk.END)

        self.once=True
        pat = self.make_regexp(types)
        os.chdir(dir_path)
        for f in os.listdir():
            if pat.search(f):
                pass
                #file = P.join(dir, f)
                #img = I.open(file)
                #ImageLabel(self.stxt, file,
                #           Itk.PhotoImage(img.resize(get_size(img.size), I.NEAREST)))

    def browse(self):
        dir_path = D.askdirectory()
        if dir_path:
            self.e_dir.delete(0, Tk.END)
            self.e_dir.insert(0, dir_path)
            subprocess.Popen(['explorer', dir_path.replace("/", "\\")])            
            self.update(dir_path, self.var_type)

    def show_sum(self, event):
        self.update(self.e_dir.get(), self.var_type)        

    def show_info(self):
        M.showinfo(u"<使い方>\n",
                   u"Entry か Browseボタンでディレクトリを選択してください。\n"
                   u"そのディレクトリに含まれるファイルの一覧が表示されます。\n"
                   u"一覧にあるファイルをダブルクリックすると、別窓でファイルが実行されます。\n"
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