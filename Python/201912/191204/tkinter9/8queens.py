#! /usr/bin/env python

"""
eight queens, whose gui uses Tkinter
"""

import tkinter as Tk
import queen as Q
import os


Q_font = ("Times", 14)



def move_queen(now, next):
    return [(i, z1-z0) for i, (z0, z1) in enumerate(zip(now, next)) if z0 != z1]



class Cboard(Tk.Canvas):
    cell_size = 46
    margin = 5
    q_images = []
    q_figure = []
    
    def __init__(self, master):
        cwidth = 8*self.cell_size 

        Tk.Canvas.__init__(self, master, relief=Tk.RAISED, bd=4, bg='white',
                            width=cwidth, height=cwidth)
                            
        self.q_answers = Q.eight_queens()
        

        for i in range(8):

            for j in range(8):
                bcolor = (i-j)%2==0 and "#699C69" or "#D4D49F"
                x0 = i*self.cell_size + self.margin
                y0 = j*self.cell_size + self.margin
                self.create_rectangle(x0, y0, x0+self.cell_size, y0+self.cell_size, fill=bcolor, width=0)

            self.q_images.append(Tk.PhotoImage(file=os.path.dirname(__file__)+"/queen.gif"))
            z =  self.q_answers[0][i]
            x = self.cell_size*(int(z / 8)+0.5) + self.margin
            y = self.cell_size*(int(z % 8)+0.5) + self.margin
            self.q_figure.append(self.create_image(x, y, image=self.q_images[i], tags="queen"))


    def refresh(self, now, next):
        answer_now = self.q_answers[now]
        answer_next = self.q_answers[now+next]
        for i, j in move_queen(answer_now, answer_next):
            self.move(self.q_figure[i], 0, j*self.cell_size) 




class Queen(Tk.Frame):

    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.master.title("8 Queens")

        
        # title
        l_title = Tk.Label(self, text='Eight Queens', font=('Times', '24', ('italic', 'bold')),
                                fg='#191970', bg='#EEE8AA', width=12)
        l_title.pack(padx=10, pady=10)

        # chess board
        self.f_board = Cboard(self)
        self.f_board.pack(padx=10, pady=10)

        # buttons and a counter
        self.q_counter = 0
        self.f_footer = Tk.Frame(self)
        self.f_footer.pack()
        self.s_counter = Tk.StringVar()
        self.s_counter.set("%d/12" % (1 + self.q_counter))
        self.a_button = Tk.Button(self.f_footer, text="next", font=Q_font, command = self.show_next)
        self.a_button.pack(side=Tk.LEFT, padx=5,pady=5)
        self.b_button = Tk.Button(self.f_footer, text="prev", font=Q_font, command = self.show_prev)
        self.b_button.pack(side=Tk.LEFT, padx=5,pady=5)
        self.f_label = Tk.Label(self.f_footer, textvariable = self.s_counter, font=Q_font)
        self.f_label.pack(side=Tk.LEFT, padx=5, pady=5)


    def show_next(self):
        if(self.q_counter < 11):
            self.f_board.refresh(self.q_counter, 1)
            self.change_counter(1)


    def show_prev(self):
        if(self.q_counter > 0):
            self.f_board.refresh(self.q_counter, -1)
            self.change_counter(-1)


    def change_counter(self, i):
        self.q_counter += i
        self.s_counter.set("%d/12" % (1 + self.q_counter))
    
            
##--------------------------------------------------- 
if __name__ == "__main__":
    app = Queen()
    app.pack()
    app.mainloop()
