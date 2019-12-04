#! /usr/bin/env python

"""
eight queens, whose gui uses Tkinter
"""

import tkinter as tk
import queen as q

#global parameter
Q_font = ("Times", 14)

# gui
class Queen(tk.Frame):
    q_counter = 0

    def init_title(self):
        self.master.title("8 Queens")
        self.f_title = tk.Frame(self)
        self.i_title = tk.PhotoImage(file="8qsubtitle.ppm")
        self.l_title = tk.Label(self.f_title, image = self.i_title)
        self.l_title.pack()
        self.f_title.pack(side=tk.TOP, padx=10, pady=10)

    def init_board(self):
        self.f_board = tk.Frame(self, relief=tk.GROOVE, bd=3)
        self.f_board.pack(side=tk.TOP, padx=10, pady=10)
        self.cell_images = [tk.PhotoImage(file=ppm) for ppm in ("bw.ppm", "bg.ppm", "qw.ppm", "qg.ppm")]
        self.q_answers = q.eight_queens()
        answer = self.q_answers[0]
        for i in range(64):
            tk.Label(self.f_board, \
              image=self.cell_images[q.qmod(i)+((i in answer) and 2 or 0)]).grid(row=int(i/8), column=int(i%8))
            
    def init_footer(self):
        self.f_footer = tk.Frame(self)
        self.f_footer.pack(side=tk.TOP, fill=tk.X, expand=1)
        self.s_counter = tk.StringVar()
        self.s_counter.set("%d/12" % (1 + self.q_counter))
        self.f_label = tk.Label(self.f_footer, textvariable = self.s_counter, font=Q_font, width=8)
        self.f_label.pack(side=tk.RIGHT, padx=10)
        self.b_button = tk.Button(self.f_footer, text="back", font=Q_font, command = self.show_prev)
        self.b_button.pack(side=tk.RIGHT, padx=1,pady=1)
        self.a_button = tk.Button(self.f_footer, text="next", font=Q_font, command = self.show_next)
        self.a_button.pack(side=tk.RIGHT, padx=1,pady=1)
            

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.init_title()
        self.init_board()
        self.init_footer()
        
#refresh board and counter
    def refresh(self, forward):
        i_now = self.q_counter
        self.q_counter += forward and 1 or -1
        self.s_counter.set("%d/12" % (1 + self.q_counter))
        a_next = self.q_answers[self.q_counter]
        a_now  = self.q_answers[i_now]
        q_or_b=0
        for cells in [q.set_difference(a_now, a_next), q.set_difference(a_next, a_now)]:
            for i in cells:
                tk.Label(self.f_board, image=self.cell_images[q.qmod(i) + q_or_b]).grid(row=int(i/8), column=int(i%8))
            q_or_b += 2
        
    def show_next(self):
        if(self.q_counter < 11):
            self.refresh(True)
            
    def show_prev(self):
        if(self.q_counter > 0):
            self.refresh(False)


if __name__ == "__main__":
    root = tk.Tk()
    que = Queen()
    que.pack()
    root.mainloop()
