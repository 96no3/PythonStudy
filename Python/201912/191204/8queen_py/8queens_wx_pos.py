#! usr/bin/env python

"""
eight queens, whose gui uses wx absolute positioning
"""
import wx
import queen as q

#global parameter
Q_font = ("Times", 14)
X_Margin = 20
Y_Margin = 20

# gui
class Board(wx.Panel):
    def init_title(self):
        self.i_title = wx.Image('8qsubtitle.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        wx.StaticBitmap(self, -1, self.i_title, \
          (5, 5), (self.i_title.GetWidth(), self.i_title.GetHeight()))
  
    def init_board(self):
        self.cell_images = [wx.Image(png, wx.BITMAP_TYPE_PNG).ConvertToBitmap() \
                                    for png in ('bw.png', 'bg.png', 'qw.png', 'qg.png')]
        answer = self.q_answers[0]
        self.i_width = self.cell_images[0].GetWidth()
        self.i_height = self.cell_images[0].GetHeight()
        for i in range(64):
            j = q.qmod(i) + (((i in answer) and 2) or 0)
            wx.StaticBitmap(self, -1, self.cell_images[j], \
              (self.i_width*int(i%8)+self.xmargin, self.i_height*int(i/8)+self.ymargin),  \
              (self.i_width,  self.i_height))

    def init_footer(self):
        self.counter = 0
        btn1 = wx.Button(self, 10, "Forward", (20, 420))
        self.Bind(wx.EVT_BUTTON, self.show_next, btn1)
        btn2 = wx.Button(self, 20, "Backward", (100, 420))
        self.Bind(wx.EVT_BUTTON, self.show_prev, btn2)
        self.label = wx.StaticText(self, -1, ("%d/12" % (self.counter+1)), (180, 430))
            
    def init_all(self):
        self.q_answers = q.eight_queens()
        self.init_title()
        self.init_board()
        self.init_footer()

    def __init__(self, frame):
        wx.Panel.__init__(self, frame, style=wx.NO_FULL_REPAINT_ON_RESIZE)
        self.xmargin = 40
        self.ymargin = 60
        self.init_all()
        self.Layout()

        
#refresh board and counter
    def refresh(self, forward):
        i_now = self.counter
        self.counter += forward and 1 or -1
        self.label.SetLabel("%d/12" % (1 + self.counter))
        a_next = self.q_answers[self.counter]
        a_now  = self.q_answers[i_now]
        q_or_b=0
        for cells in [q.set_difference(a_now, a_next), q.set_difference(a_next, a_now)]:
            for i in cells:
                j = q.qmod(i) + q_or_b
                wx.StaticBitmap(self, -1, self.cell_images[j], \
                  (self.i_width*int(i%8)+self.xmargin, self.i_height*int(i/8)+self.ymargin), \
                  (self.i_width,  self.i_height))
            q_or_b += 2
        
    def show_next(self, event):
        if(self.counter < 11):
            self.refresh(True)
            
    def show_prev(self, event):
        if(self.counter > 0):
            self.refresh(False)

        
class Queen(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, -1, "8 queens", pos=(150, 150), size=(420, 500))
        Board(frame)
        self.SetTopWindow(frame)
        frame.Show(True)
        return True
    
if __name__ == "__main__":
    que = Queen(redirect=False)
    que.MainLoop()
