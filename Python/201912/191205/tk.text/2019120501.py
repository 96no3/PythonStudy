import tkinter as Tk
import rhello as RH
import thello as TH
import timer as Ti
import tkinter.scrolledtext as S
import os

PATH = CLOCK = os.path.dirname(__file__)+"/"

## functions ------------------------------------------------------------
def read_contents(fname):
    """ read contens of `fname' """
    with open(PATH+fname, mode="r") as f:
        string = ""
        for i in f:
            string += i
    return string    

def left_slide(string):  
    ls0 = string.split('+')
    ls1 = ls0[0].split('x')
    return ('500x600+%d+%s' % (int(ls1[0]) + int(ls0[1]), ls0[2]))

## classes ---------------------------------------------------------------
class Frame(Tk.Frame):
    """ The main class of this program. """
    
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.visited=dict()
        self.code_window = None
        self.master.geometry('500x600+20+20')
        self.st = S.ScrolledText(self, padx=20, pady=25, cursor='arrow', wrap=Tk.WORD, font=('Helvetica', '12'))
        self.st.pack(fill=Tk.BOTH, expand=1)

        ### tag configuration
        self.st.tag_config('h1', font=('Helvetica', '24'), justify=Tk.CENTER)
        self.st.tag_config('h2', font=('Helvetica', '18'))
        self.st.tag_config('link', font=('Helvetica', '12'), foreground='blue', underline=1)
        self.st.tag_config('em', font=('Helvetica', '12', 'bold'), foreground="red")
        self.st.tag_config('cite', font=('Helvetica', '12'), foreground="navy")
        self.st.tag_config('var', font=('Helvetica', '12', 'bold'), foreground="darkgreen")
        self.st.tag_config('center', justify=Tk.CENTER)
        self.st.tag_bind('link', "<Double-Button-1>", self.on_clicked)
        self.st.tag_bind('link', "<Enter>", self.on_enter, '+')
        self.st.tag_bind('link', "<Leave>", self.on_leave, '+')

        ### title
        self.st.insert(Tk.END, u'Label を動かして遊んでみよう\n', 'h1' )
        hr = Tk.Frame(self.st, relief=Tk.RIDGE, height=0, width=460)
        self.st.window_create(Tk.END,  window=hr, align=Tk.CENTER)
        self.st.tag_add('center', hr)
        self.st.insert(Tk.END, u'\n')

        ### section 1
        self.st.insert(Tk.END, u'1. 初めに\n\n', 'h2' )
        self.st.insert(Tk.END,    
             u"Tk のデモのラベルの項には、 ”ラベルは動かせないからつまらない”\n")
        self.st.insert(Tk.END,    
             u"(\"Labels are pretty boring because you can't do anything with them.\")\n", 'cite')
        self.st.insert(Tk.END,    
             u"と書かれていますが、マウスのクリック、キープレスなどのイベントと結びつけると"
             u"いろいろと動かすことができます。\n"
             u"ここでは、クリックするとランダムに文字色が変わる")
        self.st.insert(Tk.END,  u'Hello world', 'var')  
        self.st.insert(Tk.END,  u'、クリックすると文字の温度が上がっていく ')  
        self.st.insert(Tk.END,  u'Hello world', 'var')  
        self.st.insert(Tk.END,  u'、クリックすると動き出す ')  
        self.st.insert(Tk.END,  u'Timer', 'var')  
        self.st.insert(Tk.END,  u' を例にとって 説明 しようと思います。 \n\n')  
             
        ## section 2
        self.st.insert(Tk.END, u'2. 色がランダムに変わるラベル\n\n', 'h2' )
        self.st.insert(Tk.END, u'とりあえず、刺激に反応するラベルを作って見ましょう。\n'
                          u'図１は一見何の変哲もない Hello world ですが、 クリック すると 背景色が変わります。\n(')
        self.st.insert(Tk.END, u'コードを見る', ('link', 'rhello.py') )
        self.st.insert(Tk.END,  ")\n\n")                          
        hello1 = RH.Label(self.st, relief=Tk.RIDGE)
        self.st.window_create(Tk.END,  window=hello1, align=Tk.CENTER, padx=20, pady=20)
        self.st.tag_add('center', hello1)
        self.st.insert(Tk.END, u'\n図１: クリックすると背景色が変わる hello world\n', 'center')
        self.st.insert(Tk.END,    u'実際にクリックしてみてください。\n背景色が変わります。\n\n'
                             , ('center','em'))

        ## section 3
        self.st.insert(Tk.END, u'3. 反応が継続するラベル\n\n', 'h2' )
        self.st.insert(Tk.END, u'次に動作が継続するラベルを作ってみましょう。\n'
                          u'図２クリックすると Hello world の文字が現れ、 文字の 温度が 徐々に上昇していきます。\n(')
        self.st.insert(Tk.END, u'コードを見る', ('link', 'thello.py') )
        self.st.insert(Tk.END,  ")\n\n")
        hello2 = TH.Frame(self.st, relief=Tk.RIDGE)
        self.st.window_create(Tk.END,  window=hello2, align=Tk.CENTER, padx=20, pady=20)
        self.st.tag_add('center', hello2)
        self.st.insert(Tk.END, u'\n図２: クリックすると文字色の温度が上がる hello world\n', 'center')
        self.st.insert(Tk.END,    u'実際にクリックしてみてください。\n文字色が変わります。\n'
                             u'右クリックで元に戻ります。\n\n', ('center','em'))
        
        ### section 4
        self.st.insert(Tk.END, u'4. Label だけでタイマーを作ろう\n\n', 'h2' )
        self.st.insert(Tk.END,    
                 u"実用的な例として、 図３に示すようなアラームクロックをラベルだけで作ってみましょう。"
                 u"このアラームはマウスの左ボタンで Start/Stop し、右ボタンで Reset します。\n(" )
        self.st.insert(Tk.END, u'コードを見る', ('link', 'timer.py') )                 
        self.st.insert(Tk.END,  ")\n\n")
        app1 = Ti.Frame(self.st, 3, relief=Tk.RIDGE)
        self.st.window_create(Tk.END,  window=app1, align=Tk.CENTER, padx=20, pady=20)
        self.st.tag_add('center', app1)
        self.st.insert(Tk.END,  "\n")
        self.st.insert(Tk.END, u'\n図３: Label だけでできたアラームクロック\n', 'center')
        self.st.insert(Tk.END,    u'実際にクリックしてみてください。\n動いたり止まったりします。\n\n', ('center','em'))
        self.st.insert(Tk.END,    u'この時計は残り 20 秒をきると、 図４を クリックした ときに 見えるように、'
                             u' 時計アイコンの背景が黄色くなります。\n')
        app2 = Ti.Frame(self.st, 0.2, relief=Tk.RIDGE)
        self.st.window_create(Tk.END,  window=app2, align=Tk.CENTER, padx=20, pady=20)
        self.st.tag_add('center', app2)
        self.st.insert(Tk.END, u'\n図４: 残り 20 秒を切ったところ。\n', 'center')
        self.st.insert(Tk.END, u'実際にクリックしてみてください。\n動いたり止まったりします。\n\n', ('center','em'))
        self.st.insert(Tk.END,    u'さらに、残り時間がなくなると、図５をクリックしたときに見えるように、'
                             u'時計アイコンの背景が赤、黄と点滅します。\n')
        app3 = Ti.Frame(self.st, 0.0, relief=Tk.RIDGE)
        self.st.window_create(Tk.END,  window=app3, align=Tk.CENTER, padx=20, pady=20)
        self.st.tag_add('center', app3)
        self.st.insert(Tk.END, u'\n図５: 残時間がなくなったところ。\n', 'center')
        self.st.insert(Tk.END, u'実際にクリックしてみてください。\n動いたり止まったりします。\n\n', ('center','em'))

        ### section 5
        self.st.insert(Tk.END, u'5. 終わりに\n\n', 'h2' )
        self.st.insert(Tk.END, u'Tk.Label だけでも動かせるアプリを作れることがお分かりいただけたと思います。\n'
                          u'また、Tk.Text を使うと インターラクティブな 説明が できることが お分かりいただけたと思います。\n\n'
        )
        self.st.configure(state=Tk.DISABLED)

    ##----
    def on_leave(self, event):
        self.st.tag_config(self.link, foreground=self.link in self.visited and 'deepskyblue' or 'blue')        
        
    def on_clicked(self, event):
        if self.code_window and self.code_window.winfo_exists():
            self.code.delete('1.0', Tk.END)
        else:
            self.code_window = Tk.Toplevel()
            self.code_window.geometry(left_slide(self.master.winfo_geometry()))
            self.code = S.ScrolledText(self.code_window, wrap=Tk.WORD)
            self.code.pack(fill=Tk.BOTH, expand=1)
            
        self.code_window.title(self.link)
        self.code.insert(Tk.END, read_contents(self.link))
        self.code_window.focus_set()
        self.visited[self.link]=True
        
    def on_enter(self, event):
        tags = self.st.tag_names(Tk.CURRENT)
        self.link = tags[-1]
        self.st.tag_config(self.link, foreground="#FF0099")
        
##------------------------------------------------ 
if __name__ == '__main__':
    f = Frame()
    f.pack(fill=Tk.BOTH, expand=1)
    f.mainloop()