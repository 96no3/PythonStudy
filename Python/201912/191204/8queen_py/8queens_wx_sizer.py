#! usr/bin/env python

"""
eight queens, whose gui uses wx sizer
"""

import wx, wx.lib.rcsizer
import queen as q
#global parameter
Q_font = ("Times", 14)

# gui
class Board(wx.Panel):
    def __init__(self, frame):
        #  8 queens answers
        self.q_answers = q.eight_queens()
        answer = self.q_answers[0]
        self.counter = 0

        # images
        #title
        self.i_title = wx.Image('8qsubtitle.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        #cell
        self.cell_images = [wx.Image(png, wx.BITMAP_TYPE_PNG).ConvertToBitmap() \
                                    for png in ('bw.png', 'bg.png', 'qw.png', 'qg.png')]

        # Panel
        wx.Panel.__init__(self, frame, -1)
        self.box = wx.BoxSizer(wx.VERTICAL)  

        # Title
        self.box.Add(wx.StaticBitmap(self, -1, self.i_title), \
          0, wx.ALIGN_CENTER | wx.ALL, 10)

        #Chess Board
        self.grid = wx.lib.rcsizer.RowColSizer()

        for i in range(64):
            j = q.qmod(i) + ((i in answer) and 2 or 0)
            self.grid.Add(  \
              wx.StaticBitmap(self, -1, self.cell_images[j]), \
              flag=wx.EXPAND, row=int(i/8), col=int(i%8))

        self.box.Add(self.grid, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        
        # Footer
        self.footer = wx.BoxSizer(wx.HORIZONTAL)
        
        btn1 = wx.Button(self, wx.ID_FORWARD, "")
        self.Bind(wx.EVT_BUTTON, self.show_next, btn1)
        self.footer.Add(btn1, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        
        btn2 = wx.Button(self, wx.ID_BACKWARD, "")
        self.Bind(wx.EVT_BUTTON, self.show_prev, btn2)
        self.footer.Add(btn2, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        
        self.label = wx.StaticText(self, -1, ("%d/12" % (self.counter+1)))
        self.footer.Add(self.label, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)

        self.box.Add(self.footer, 0,  wx.ALIGN_CENTER | wx.ALL, 10)

        # Layout
        self.SetSizer(self.box)
#        self.Bind(wx.EVT_SIZE, self.on_size)
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
                self.grid.Add(  \
                  wx.StaticBitmap(self, -1, self.cell_images[j]), \
                  flag=wx.EXPAND, row=int(i/8), col=int(i%8))
            q_or_b += 2
      #  self.SetSizer(self.box)
        self.Layout()
        
    def show_next(self, event):
        if(self.counter < 11):
            self.refresh(True)
            
    def show_prev(self, event):
        if(self.counter > 0):
            self.refresh(False)

#    def on_size(self, event):
#        self.Layout()
#        self.Refresh()
        
class Queen(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, -1, "8 queens" , size=(450,500),  \
                          style=wx.DEFAULT_FRAME_STYLE | wx.ST_NO_AUTORESIZE)
        Board(frame)
        self.SetTopWindow(frame)
        frame.Show(True)
        return True
    
if __name__ == "__main__":
    que = Queen(redirect=False)
    que.MainLoop()
