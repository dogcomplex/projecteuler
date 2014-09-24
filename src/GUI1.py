'''
Created on May 13, 2011

@author: W
'''

'''
class MyFrame(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self, parent, id, title, (-1, -1), wx.Size(600, 600))
        panel = wx.Panel(self, -1)
        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(wx.Button(panel, 1, 'Reset'), 1 )
        box.Add(wx.Button(panel, 2, 'Run'), 1 )
        panel.SetSizer(box)
        
        self.point = wx.Bitmap('dot.bmp')
        self.Bind(wx.EVT_BUTTON, self.OnRun, id=1)
        #self.Bind(wx.EVT_BUTTON, self.OnReset, id=1)
        self.Bind(wx.EVT_BUTTON, self.OnReset, id=2)
        self.Bind(wx.EVT_PAINT, self.OnRun)

'''


import wx

class DrawPanel(wx.Frame):
    """Draw a line to a panel."""
    def __init__(self):
        wx.Frame.__init__(self, title="Draw on Panel")
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event=None):
        dc = wx.PaintDC(self)
        dc.Clear()
        dc.SetPen(wx.Pen(wx.BLACK, 4))
        dc.DrawLine(0, 0, 50, 50)

app = wx.App(False)
frame = DrawPanel()
frame.Show()
app.MainLoop()