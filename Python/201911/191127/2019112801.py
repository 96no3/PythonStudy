#! /usr/bin/env python

import tkinter as Tk
from PIL import Image as I
from PIL import ImageTk as Itk
import math
import os

FLOWERPATH = os.path.dirname(__file__)+"/flower/"
FLOWERS = ["suisencut4.gif", "tanpopotouka1.gif", "odamakitouka.gif", "rengetouka2.gif",              \
           "ajisaicatmurasaki-a.gif", "cosmos-s.gif", "fujimurasakitouka.gif", "minaesi-5.gif",       \
           "hotarubukuro3ko.gif", "burudejinarabi.gif", "aoaji3touka.gif", "sakurasou.gif",           \
           "rengetakusann.gif", "nanohana3.gif", "suzurantouka2.gif", "liradai.gif",                  \
           "cosmostouka-b.gif", "syunrantouka2.gif", "sakuraeda9.gif", "syoubu-s.gif",                \
           "suirenpink-a.gif", "yuri2.gif", "aoasagaoline.gif", "asagaoyoujiro2.gif",                 \
           "himawari-l.gif", "yagurumagikutouka1.gif", "susukistouka.gif"]

SIZE = 100

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

class Frame(Tk.Frame):    
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.master.title('show flower images')
        intro = Tk.Label(self, font=('Helvetica', '12'),  justify=Tk.LEFT, wraplength='15c', width=50, 
                         text = u"リストボックスから画像ファイルを選択してください。\n"
                                u"左ボタンのドラッグ、Shift + 左ボタン、Ctrl + 左ボタン などで複数の画像の選択が可能です。\n"
                                u"選択が終わったら、マウス右ボタンをクリックしてください。\n" 
                                u"選択された画像が右側に表示されます。\n")
        intro.pack()
        self.f = Tk.Frame(self, bd=3, relief=Tk.RIDGE)
        self.f.pack(fill=Tk.BOTH, expand=1)
        
        f_lb = Tk.Frame(self.f)
        f_lb.pack(side=Tk.LEFT, padx=5, pady=5, fill=Tk.BOTH, expand=1)

        self.listbox = Tk.Listbox(f_lb,selectmode=Tk.EXTENDED)
        self.listbox.pack(side=Tk.LEFT, fill=Tk.Y, expand=1)
        self.listbox.bind("<3>", self.show_flowers)
        self.listbox.insert(Tk.END, *FLOWERS)

        self.scrollbar = Tk.Scrollbar(f_lb, orient=Tk.VERTICAL,command=self.listbox.yview)
        self.listbox['yscrollcommand'] = self.scrollbar.set
        self.scrollbar.pack(side=Tk.RIGHT, fill=Tk.Y, expand=1)

        self.renew()

    def show_flowers(self, event):
        if self.images:
            self.ff.destroy()
            self.renew()
            
        selected = [ int(x) for x in self.listbox.curselection()]
        span = int(math.ceil(math.sqrt(len(selected))))
        if span == 0:
            return None

        for i, j in  enumerate(selected):
            img = I.open(FLOWERPATH+FLOWERS[j])
            img = img.resize(get_size(img.size))
            tkimg = Itk.PhotoImage(img)
            la = Tk.Label(self.ff, image=tkimg)
            la.grid(row=int(i/span), column=int(i%span), sticky=Tk.SW)
            self.images.append(tkimg)
        self.listbox.selection_clear(min(selected), max(selected))
   
    def renew(self):
        self.images = []
        self.ff = Tk.Frame(self.f, border=3, relief=Tk.RAISED)
        self.ff.pack(side=Tk.RIGHT, fill=Tk.BOTH, expand=1, padx =5)

if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()
