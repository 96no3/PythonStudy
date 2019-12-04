#! /usr/bin/env python

"""
eight queens, whose gui uses Tkinter
"""

import tkinter as tk
import queen as q

#global parameter
Q_font = ("Times", 14)

# gui

class Cboard(tk.Canvas):
    cell_size = 46
    margin = 5
    q_map = dict() # position -> id
    q_images = dict()
    def __init__(self, master):
        cwidth = 8*self.cell_size 
        cheight = cwidth

        tk.Canvas.__init__(self, master, relief=tk.RAISED, bd=4, bg="#FFFFFF",
                            width=cwidth, height=cheight)

        for i in range(8):
            for j in range(8):
                if((i-j)%2==0) :
                    bcolor = "#699C69"
                else:
                    bcolor = "#D4D49F"
                x0 = i*self.cell_size + self.margin
                y0 = j*self.cell_size + self.margin
                self.create_rectangle(x0, y0, x0+self.cell_size, y0+self.cell_size, fill=bcolor, width=0)

    def put_queens(self, q_add, q_del):
        for x in q_del:
            self.delete(self.q_map[x])
            del self.q_map[x]
        
        for x in q_add:
            self.q_map[x] = self.put_a_queen(x)



            
    def put_a_queen(self, z):
        self.q_images[z] = tk.PhotoImage(file="q.gif")
        i = int(z % 8)
        j = int(z / 8)
        x = self.cell_size*(i+0.5) + self.margin
        y = self.cell_size*(j+0.5) + self.margin
        return self.create_image(x,y,image=self.q_images[z],tags="queen")
                          



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
        self.f_board = Cboard(self)
        self.f_board.pack(side=tk.TOP, padx=10, pady=10)
        self.f_board.put_queens(self.q_answers[0], [])


        

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
        self.q_answers = q.eight_queens()
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
        self.f_board.put_queens(q.set_difference(a_next, a_now), q.set_difference(a_now, a_next))



        
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
