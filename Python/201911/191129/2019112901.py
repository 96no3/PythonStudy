import re
import os
import os.path as P
import tkinter as Tk
from PIL import Image as I
from PIL import ImageTk as Itk
import tkinter.filedialog as D
import tkinter.messagebox as M

SIZE = 100
IMAGR_TYPES = ['gif', 'png', 'bmp', 'jpg', 'tif', 'ppm']
MAM_COLN = 6
GEO_MAIN = '+20+20'
GEO_SATE = '+750+50'
GEO_SCAL = '+750+400'
BGS = [('aliceblue', '#F0F8FF'), ('azure', '#F0FFFF'), ('beige', '#F5F5DC'),              \
       ('cornsilk', '#FFF8DC'), ('khaki', '#F0E68C'), ('lightgreen', '#90EE90'),          \
       ('lightpink', '#FFB6C1'), ('lightskyblue', '#87CEFA'), ('palegreen', '#98FB98')]

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
    
    def __init__(self, master, image_file, img):
        Tk.Frame.__init__(self, master)
        self.image = img # 一覧で表示する Tk.Image
        self.image_file = image_file # もとのイメージファイル
        img_label=Tk.Label(self, image=self.image)
        img_label.pack()
        txt_label=Tk.Label(self, text=P.basename(self.image_file), font=('Helvetica', '8'))
        txt_label.pack()
        img_label.bind('<Double-Button-1>', self.show)

    def show(self, event):
        label = ImageLabel.id_original_size
        if (label and label.winfo_exists()):
            top = label.winfo_toplevel()
            top.destroy()
        top = Tk.Toplevel(self)
        top.title(P.basename(self.image_file))
        top.geometry(GEO_SATE)
        img = I.open(P.abspath(self.image_file))
        self.timg = Itk.PhotoImage(img)
        label=Tk.Label(top, image=self.timg, bg=ImageLabel.bg_var.get())
        label.pack()
        ImageLabel.id_original_size = label

class ImageFrame:
    """ A Class to show summary of images """
    
    def __init__(self, master, **key):
        self.master=master
        self.key = key
        self.frame=Tk.Frame(master, **key)
        self.frame.pack(padx=5, pady=5)
        self.once = False

    def update(self, dir, types):
        if self.once:
            self.frame.destroy()
            self.frame=Tk.Frame(self.master, **self.key)
            self.frame.pack(padx=5, pady=5)
        self.once = True
        pat = make_regexp(types)
        files = [P.join(dir, file) for file in os.listdir(dir) if pat.search(file)]
        for i, file in enumerate(files):
            img_temp = I.open(file)
            img = img_temp.resize(get_size(img_temp.size), I.NEAREST)  
            tkimg = Itk.PhotoImage(img)
            la = ImageLabel(self.frame, file, tkimg)
            la.grid(row = int(i/MAM_COLN), column=int(i%MAM_COLN), sticky=Tk.S+Tk.W+Tk.E)

class Frame(Tk.Frame):
    """ The main class of this program. """
    
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.master.title('Image Viewer')
        self.master.geometry(GEO_MAIN)
        self.cus_top = None # 背景色調節 window をあらわす内部変数

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
        for image_type in IMAGR_TYPES:
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
