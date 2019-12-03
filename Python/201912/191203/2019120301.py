import tkinter as Tk
import tkinter.dialog as D

class Frame (Tk.Frame):
    FLOWERS = [u'あさがお', u'タンポポ', u'ゆり', u'はす', u'桜']

    def __init__(self, master=None, **key):
        Tk.Frame.__init__(self, master, **key)
        self.master.title(u'好きな花はなんですか?')
        self.master.geometry("280x30")
        svar = Tk.StringVar()
        label = Tk.Label(textvariable=svar, font=('Helvetica', '12'))
        label.pack(fill=Tk.BOTH, expand=1)
        dialog = D.Dialog(self, title=u'好きな花',
                            text=u'下のボタンから好きな花を選んでください。',
                            bitmap='question',
                            default=0,
                            strings=self.FLOWERS)
        svar.set(u'%s がお好きなのですね。' % self.FLOWERS[dialog.num])

if __name__=='__main__':
    f = Frame()
    f.pack(fill=Tk.BOTH, expand=1)
    f.mainloop()