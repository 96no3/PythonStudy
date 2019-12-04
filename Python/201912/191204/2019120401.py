import tkinter as Tk

class Gboard(Tk.Canvas):
    """Tk.Canvas for Go Board"""
    grid_size = 20
    stones = dict()

    def __init__(self, master=None):
        en = self.grid_size * 19
        z = self.grid_size * 0.36
        hosi = 2
        Tk.Canvas.__init__(self, master, relief=Tk.RAISED, bd=4, bg="#F7EE8A",
                            width=20*self.grid_size, height=20*self.grid_size, highlightthickness=0)
        
        # binding the goban canvas to put_stones method
        self.bind("<1>", self.put_stones)
        # drawing lines and coordinate
        for i in range(19):
            x= (i+1) * self.grid_size
            self.create_line(x, self.grid_size, x, en)
            self.create_line( self.grid_size, x, en, x)
            self.create_text(z, x, text=str(i), justify=Tk.RIGHT, fill="#002010",
                            font = ("Helvetica","6","normal"))
            self.create_text(x, z , text=str(i), justify=Tk.CENTER, fill="#002010",
                            font = ("Helvetica","6","normal"))
        
        # drawing black dots
        for i in range(4,17,6):
            for j in range(4,17,6):
                x = i * self.grid_size
                y = j * self.grid_size
                self.create_oval(x-hosi, y-hosi, x+hosi, y+hosi, fill= "black")
    
    def bclear(self):
        """ clear stones in the map and on the canvas"""
        self.stones.clear()
        self.delete("stone")

    def bopen (self, fname):
        """open *.gbn file, whose content is ( [kuro ishi positions], [shiro ishi positions])"""
        with open(fname,"r") as fp:
            for i,pos in enumerate(fp):
                if i == 1:
                    lb=pos
                elif i == 2:
                    lw=pos
        
        for row, col in lb:
            self.stones[(row,col)] = self.put_a_stone(row, col, "black")
        for row, col in lw:
            self.stones[(row,col)] = self.put_a_stone(row, col, "white")
    
    def bsave(self, fname):
        """ save positions of stones in a file """
        lb = []
        lw = []
        for key, val in self.stones.items():
            if self.itemcget(val, "fill") == "black":
                lb.append(key)
            else:
                lw.append(key)

        with open(fname,"w") as fp:
            fp.write("[black stones], [white stones]\n")
            fp.write(str(lb))
            fp.write("\n")
            fp.write(str(lw))
            fp.write("\n")

    def put_stones(self, event):
        """ putting go ishis on the goban,
            this function is bounded to the left one click of the mouse"""
        cx = self.canvasx(event.x, self.grid_size)
        cy = self.canvasy(event.y, self.grid_size)
        col = int(cx/self.grid_size) - 1
        row = int(cy/self.grid_size) - 1
        if (0<=row<=18 and 0<=col<=18):
            if (not ((row,col) in self.stones)):
                self.stones[(row,col)] = self.put_a_stone(row, col, "black")
            elif(self.itemcget(self.stones[(row,col)], "fill") == "black"):
                self.itemconfig(self.stones[(row,col)], fill="white")
            else:
                self.delete(self.stones[(row,col)])
                del self.stones[(row,col)]
    
    def put_a_stone(self, row, col, color):
        """ it drows a go-ishi on the goban canvas and returns the go-ishi's ID """
        r = self.grid_size * 0.45
        x_left = (col+1)*self.grid_size-r
        x_right = (col+1)*self.grid_size+r
        y_top = (row+1)*self.grid_size-r
        y_bottom = (row+1)*self.grid_size+r
        return self.create_oval(x_left, y_top, x_right, y_bottom, fill = color, tags = "stone")

    def add_n_on_stone(self, i, row, col, tcolor):
        """ draw number of a stone """
        return self.create_text((col+1)*self.grid_size, (row+1)*self.grid_size,
                                text=str(i+1), justify=Tk.CENTER, fill=tcolor,
                                font = ("Helvetica","8","bold"), tags="stone")

if __name__ == "__main__":
    board = Gboard()
    board.pack()
    board.mainloop()
