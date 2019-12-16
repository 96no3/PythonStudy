import re
import os
import os.path as P
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
GEO_MAIN = '+20+20'
GEO_SATE = '+750+50'

## functions ------------------------------------------------
def make_regexp(types):
    """ It returns the regular expression of the image file type"""
    str = "\.("
    for k, v in types.items():
        if v.get():
            str += k + '|'

    str = str[0:-1] + ')$'
    return re.compile(str, re.I)

## classes ------------------------------------------------------------------
class Frame(Tk.Frame):
    """ The main class of this program. """

    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.master.title('Organize Files')
        self.master.geometry(GEO_MAIN)
        self.create_menu()
        self.create_widgets()

    def create_menu(self):
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
        b_custom_bg = Tk.Button(f, text='Customize Background', command=self.cus_bg)
        b_custom_bg.pack(side=Tk.LEFT, anchor=Tk.S, padx=10)

        self.var_type = dict()
        for image_type in IMAGE_TYPES:
            self.var_type[image_type] = Tk.IntVar()
            cb = Tk.Checkbutton(f_type, text=image_type, variable=self.var_type[image_type],
                                relief=Tk.FLAT, justify = Tk.LEFT)
            cb.select()
            cb.pack(side=Tk.LEFT, padx=5)

        ImageLabel.bg_var = Tk.StringVar()
        ImageLabel.bg_var.set('#FFFFFF')

        self.f_bg = Tk.LabelFrame(self, text='Background')
        self.f_bg.pack(anchor=Tk.W, padx=10, pady=2)

        for name, code in BGS:
            rb = Tk.Radiobutton(self.f_bg, text=name, variable=ImageLabel.bg_var, value=code,
                                bg=code, command=self.change_bg, bd=1, relief=Tk.GROOVE)
            rb.pack(side=Tk.LEFT, padx=5)

        self.image_frame = ImageFrame(self, relief=Tk.RIDGE, border=2)

    def change_bg(self):
        bg1 = ImageLabel.bg_var.get()
        label = ImageLabel.id_original_size
        if label and label.winfo_exists():
            label.configure(bg=bg1)
            top = label.winfo_toplevel()
            top.focus_set()

    def browse(self):
        dir = D.askdirectory()
        if dir:
            self.e_dir.delete(0, Tk.END)
            self.e_dir.insert(0, dir)
            self.image_frame.update(dir, self.var_type)

    def show_sum(self, event):
        self.image_frame.update(self.e_dir.get(), self.var_type)        

    def show_info(self):
        M.showinfo(u"使い方",  u"Entry か Browse ボタンでディレクトリを選択してください。\n"
                               u"そのディレクトリに含まれる画像ファイルの一覧が表示されます。\n"
                               u"一覧にある画像をクリックすると、別窓でオリジナルサイズの画像が表示されます。\n"
                               u"透過型 GIF の場合は背景色を変えることができます。\n"
                               u"ラジオボタンにある背景色が気に入らない場合は、\n"
                               u"Customize Background ボタンを押して現れる\n赤、緑、青用の３つのスケールで"
                               u"背景色を調節してください。")

    def cus_bg(self):
        if not (self.cus_top and  self.cus_top.winfo_exists()):
            self.cus_top = Tk.Toplevel(self)
            self.cus_top.title('Create Back Ground')
            self.cus_top.geometry(GEO_SCAL)
            cusf = Tk.Frame(self.cus_top)
            cusf.pack(fill=Tk.BOTH, padx=10, pady=10)
            self.scale = dict()
            for i, color in enumerate(('red', 'green', 'blue')):
                l=Tk.Label(cusf, text=color+': ', anchor=Tk.W, fg=color, font=('Helvetica', '10', 'bold'))
                l.grid(row=i, column=0, sticky=Tk.W)
                self.scale[color] = Tk.Scale(cusf, orient=Tk.HORIZONTAL, length=300, from_=0, to=255, 
                                             command=self.customize_bg, tickinterval=50)
                self.scale[color].set(255)
                self.scale[color].grid(row=i, column=1)

            self.cus_top.bind('<FocusIn>', self.customize_bg)

    def customize_bg(self, event):
        ImageLabel.bg_var.set('#%02X%02X%02X' %
                        (self.scale['red'].get(), self.scale['green'].get(), self.scale['blue'].get()))
        self.change_bg()

##------------------------------------------------ 
if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()