#! /usr/bin/env python

import tkinter as Tk
import os

FLOWERPATH = os.path.dirname(__file__)+"/flower/"
FLOWERS = ["suisencut4.gif", "tanpopotouka1.gif", "odamakitouka.gif", "rengetouka2.gif",              \
           "ajisaicatmurasaki-a.gif", "cosmos-s.gif", "fujimurasakitouka.gif", "minaesi-5.gif",       \
           "hotarubukuro3ko.gif", "burudejinarabi.gif", "aoaji3touka.gif", "sakurasou.gif",           \
           "rengetakusann.gif", "nanohana3.gif", "suzurantouka2.gif", "liradai.gif",                  \
           "cosmostouka-b.gif", "syunrantouka2.gif", "sakuraeda9.gif", "syoubu-s.gif",                \
           "suirenpink-a.gif", "yuri2.gif", "aoasagaoline.gif", "asagaoyoujiro2.gif",                 \
           "himawari-l.gif", "yagurumagikutouka1.gif", "susukistouka.gif"]

BGS = [('aliceblue', '#F0F8FF'), ('azure', '#F0FFFF'), ('beige', '#F5F5DC'),              \
       ('cornsilk', '#FFF8DC'), ('khaki', '#F0E68C'), ('lightgreen', '#90EE90'),          \
       ('lightpink', '#FFB6C1'), ('lightskyblue', '#87CEFA'), ('palegreen', '#98FB98')]

class Frame(Tk.Frame):    
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.master.title('flower image and background')
        intro = Tk.Label(self, font=('Helvetica', '12'),  justify=Tk.LEFT, wraplength='15c', 
                         text = u"リストボックスから画像ファイル（マウス左ダブルクリック）を\n"
                                u"ボタンから背景色を選択してください。\n" 
                                u"右側のラベルに画像が表示されます。\n")
        intro.pack()
        f = Tk.Frame(self, bd=3, relief=Tk.RIDGE)
        f.pack(fill=Tk.BOTH, expand=1)
        
        f_lb = Tk.Frame(f)
        f_lb.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)

        self.listbox = Tk.Listbox(f_lb)
        self.listbox.pack(side=Tk.LEFT, padx=5, pady=5, fill=Tk.Y)
        self.listbox.bind("<Double-Button-1>", self.change_flower)
        self.listbox.insert(Tk.END, *FLOWERS)

        self.scrollbar = Tk.Scrollbar(
        f_lb, orient=Tk.VERTICAL,command=self.listbox.yview)
        self.listbox['yscrollcommand'] = self.scrollbar.set
        self.scrollbar.pack(side=Tk.RIGHT, fill=Tk.Y, expand=1)

        f_button = Tk.Frame(f)
        f_button.pack(side=Tk.LEFT, padx=5, pady=5)
        self.flower = Tk.PhotoImage(file=FLOWERPATH+FLOWERS[0])
        self.label = Tk.Label(f, image=self.flower, relief=Tk.RAISED, bd=3)
        self.label.pack(side=Tk.RIGHT, padx =5, fill=Tk.BOTH, expand=1)

        for name, code in BGS:
            b = Tk.Button(f_button, text=name, bg=code, command=self.bgchange(code))
            b.pack(fill=Tk.X)
    
    def bgchange(self,color):
        def f():
            self.label.configure(bg=color)
        return f

    def change_flower(self, event):
        self.flower = Tk.PhotoImage(file=FLOWERPATH+self.listbox.get(Tk.ACTIVE))
        self.label.configure(image=self.flower)

if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()
