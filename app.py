import wx
from check import Checker
import threading
import sys


class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Checker')
        panel = wx.Panel(self)

        self.my_sizer = wx.BoxSizer(wx.VERTICAL)
        self.url_input = wx.TextCtrl(panel)
        self.url_label = wx.StaticText(panel, label="URL")
        self.my_sizer.Add(self.url_label, 0, wx.ALL | wx.EXPAND, 5)
        self.my_sizer.Add(self.url_input, 0, wx.ALL | wx.EXPAND, 5)

        self.tag_input = wx.TextCtrl(panel)
        self.tag_label = wx.StaticText(panel, label="TAG")
        self.my_sizer.Add(self.tag_label, 0, wx.ALL | wx.EXPAND, 5)
        self.my_sizer.Add(self.tag_input, 0, wx.ALL | wx.EXPAND, 5)  

        my_btn = wx.Button(panel, label='Check')
        my_btn.Bind(wx.EVT_BUTTON, self.OnClicked)
        self.my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)        
        panel.SetSizer(self.my_sizer)      

        self.logs = wx.StaticText(panel, label="")
        self.my_sizer.Add(self.logs, 0, wx.ALL | wx.EXPAND, 5)

        self.Show()

    def OnClicked(self, event): 
        if self.url_input.Value == "" or self.tag_input.Value == "":
            self.Error("Fill the inputs", "Input error")
        else:
            args = (self.url_input.Value, self.tag_input.Value, self)
            self.t = threading.Thread(target=checker.Check, args=args)
            self.t.start()

    def Print(self, msg: str):
        self.logs.Label = msg
        
    def Error(self, msg: str, title: str):
        wx.MessageBox(msg, title, wx.OK | wx.ICON_ERROR)





if __name__ == '__main__':
    checker = Checker()
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
    checker.Check = False