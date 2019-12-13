import re
import os
import os.path as P
import tkinter as Tk
from PIL import Image as I
from PIL import ImageTk as Itk
from PIL import ImageColor as Ic
import tkinter.scrolledtext as S
import tkinter.filedialog as D
import tkinter.messagebox as M

SIZE = 100
IMAGR_TYPES = ['gif', 'png', 'bmp', 'jpg', 'tif', 'ppm']
MAM_COLN = 6
GEO_MAIN = '680x600+20+20'
GEO_SATE = '+730+50'
GEO_SCAL = '+730+400'

## functions ------------------------------------------------
def get_size(tup):
    """ It returns the size of images on the summary"""
    x, y = tup
    if (x<=100 and y<=100):
        return (x, y)
    elif x > y:
        r = float(SIZE) / float(x)
        return (100, int(y*r))
    else:
        r = float(SIZE) / float(y)
        return (int(x*r), 100)        

def make_regexp(types):
    """ It returns the regular expression of the image file type"""
    str = "\.("
    for k, v in types.items():
        if v.get():
            str += k + '|'

    str = str[0:-1] + ')$'
    return re.compile(str, re.I)

## classes ------------------------------------------------------------------
class ImageLabel(Tk.Frame):
    """ A Label class to show an image """
    # 一覧表示する画像のクラス.クリックされると原寸大のイメージを別窓で表示.

    id_original_size = None    # Label showing an original size image
    bg_var = None              # variable for background color
    image_file_now = None
    
    def __init__(self, stxt, image_file, img):
        self.image = img # 一覧で表示する Tk.Image
        self.image_file = image_file # もとのイメージファイル
        frame = Tk.Frame(stxt, height=115, width=100)
        frame.pack_propagate(0)
        txt_label=Tk.Label(frame, text=P.basename(self.image_file), font=('Helvetica', '8'))
        txt_label.pack(side=Tk.BOTTOM)
        self.img_label=Tk.Label(frame, image=self.image)
        self.img_label.pack(side=Tk.BOTTOM)

        stxt.window_create(Tk.END, align=Tk.BASELINE, padx=5, pady=5, window=frame)
        self.img_label.bind('<Double-Button-1>', self.show)

    def show(self, event):
        label = ImageLabel.id_original_size
        if (label and label.winfo_exists()):
            top = label.winfo_toplevel()
            top.destroy()
        top = Tk.Toplevel(self.img_label)
        top.title(P.basename(self.image_file))
        top.geometry(GEO_SATE)
        img = I.open(P.abspath(self.image_file))
        self.timg = Itk.PhotoImage(img)
        label=Tk.Label(top, image=self.timg, bg=ImageLabel.bg_var.get())
        label.pack()
        ImageLabel.id_original_size = label
        ImageLabel.image_file_now = self.image_file

class Frame(Tk.Frame):
    """ The main class of this program. """
    
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.master.title('BackGrounder')
        self.master.geometry(GEO_MAIN)
        self.cus_top = None # 背景色調節 window をあらわす内部変数
        self.fout = None

        ### Menu
        menu_bar = Tk.Menu(self, tearoff=0)
        # File
        menu_file = Tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=menu_file,  underline=0)
        menu_file.add_command(label="Browse Dir.", command=self.browse, underline=0, accelerator = 'Ctrl-O')
        menu_file.add_command(label="ReLoad", command=self.load_dir, underline=0, accelerator = 'Ctrl-R')
        menu_file.add_command(label="Save As", command=self.save_image, underline=0, accelerator = 'Ctrl-S')
        menu_file_type = Tk.Menu(menu_file, tearoff=0)
        menu_file.add_cascade(label="File Type", menu=menu_file_type, underline=0)
        menu_file.add_separator()
        menu_file.add_command(label="Exit", command=self.exit, underline=0 , accelerator = 'Ctrl-Q')

        menu_bar.add_command(label="Back Ground", command=self.cus_bg, underline=0)
        menu_bar.add_command(label="Help", command=self.show_info, underline=0)

        # short-cuts
        self.master.bind('<Control-KeyPress-o>', self.browse)
        self.master.bind('<Control-KeyPress-s>', self.save_image)
        self.master.bind('<Control-KeyPress-r>', self.load_dir)
        self.master.bind('<Control-KeyPress-q>', self.exit)

        # check buttons in menu_file_type
        self.var_type = dict()
        for i, image_type in enumerate(IMAGR_TYPES):
            self.var_type[image_type] = Tk.IntVar()
            menu_file_type.add_checkbutton(label=image_type, variable=self.var_type[image_type])
            menu_file_type.invoke(i)

        ImageLabel.bg_var = Tk.StringVar()
        ImageLabel.bg_var.set('#FFFFFF')

        # add menu bar
        try:
            self.master.config(menu=menu_bar)     # this required to show the menu bar
        except AttributeError:
            self.master.Tk.call(master, "config", "-menu", menu_bar)

        f_type = Tk.LabelFrame(self, text='File Type')
        f_type.pack(padx=10, pady=2)
        self.e_type = Tk.Entry(f_type, width=10)
        self.e_type.pack(side=Tk.LEFT)
        for file_type in IMAGR_TYPES:
            cb = Tk.Checkbutton(f_type, text=file_type, variable=self.var_type[file_type],
                                relief=Tk.FLAT, justify = Tk.LEFT)
            cb.pack(side=Tk.LEFT, padx=5) 

        self.once = False
        self.stxt = S.ScrolledText(self, bg=self.cget('bg'), cursor=self.cget('cursor'), state=Tk.DISABLED)
        self.stxt.pack(fill=Tk.BOTH, expand=1)
        self.pack(fill=Tk.BOTH, expand=1)

    def update(self, dir, types):
        self.stxt.configure(state=Tk.NORMAL)
        if self.once:
            self.stxt.delete('1.0', Tk.END)

        self.once=True
        pat = make_regexp(types)

        for f in os.listdir(dir):
            if pat.search(f):
                file = P.join(dir, f)
                img = I.open(file)
                ImageLabel(self.stxt, file,
                           Itk.PhotoImage(img.resize(get_size(img.size), I.NEAREST)))

        self.stxt.configure(state=Tk.DISABLED)

    def browse(self, event=None):
        self.dir = D.askdirectory()
        if self.dir:
            self.load_dir()
    
    def load_dir(self, event=None):
        self.update(self.dir, self.var_type)

    def show_info(self):
        M.showinfo(u"使い方",  u"メニューバーの File->Browse Dir. でディレクトリを選択してください。\n"
                               u"そのディレクトリに含まれる画像ファイルの一覧が表示されます。\n"
                               u"一覧にある画像をクリックすると、別窓でオリジナルサイズの画像が表示されます。\n\n"
                               u"透過型 GIF の場合は背景色をつけることができます。\n"
                               u"メニューバーの Back Ground をクリックすると\n"
                               u"赤、緑、青用の３つのスケールがある Window が現れるので、\n"
                               u"それで背景色を調節できます。\n\n"
                               u"背景色をつけた画像は File->SaveAs により保存することができます。"
                               )

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

            #self.cus_top.bind('<FocusIn>', self.customize_bg)

    def customize_bg(self, event):
        ImageLabel.bg_var.set('#%02X%02X%02X' %
                        (self.scale['red'].get(), self.scale['green'].get(), self.scale['blue'].get()))
        self.change_bg()

    def change_bg(self):
        bg1 = ImageLabel.bg_var.get()
        label = ImageLabel.id_original_size
        if label and label.winfo_exists():
            label.configure(bg=bg1)
            top = label.winfo_toplevel()
            top.focus_set()

    def save_image(self, event=None):
        self.fout = D.asksaveasfilename(initialdir=self.dir, initialfile=self.fout and P.basename(self.fout) or None)
        if self.fout:
            img=I.open(ImageLabel.image_file_now)
            imgc = img.mode == 'RGB' and img or img.convert('RGB')
            bg1 = Ic.getrgb(ImageLabel.bg_var.get())         # background color
            ls=[]                                            # a sequence to store image data
            for c0 in imgc.getdata():
                if(c0==(255,255,255)):
                    ls.append(bg1)
                else:
                    ls.append(c0)
                    
            imgc.putdata(ls)
            imgc.save(self.fout)

    def exit(self, event=None):
        self.master.destroy()

##------------------------------------------------ 
if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()
