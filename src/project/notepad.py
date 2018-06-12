# -*- coding: utf-8 -*-
# @Version: Python3.6.5
# @Time: 6/11/2018 10:16 PM
# @Author  : Jacklyn

import wx
import notepadGUI

class CalcFrame(notepadGUI.MyFrame1):
    def __init__(self,parent):
        notepadGUI.MyFrame1.__init__(self,parent)

app = wx.App(False)
frame=CalcFrame(None)
frame.Show(True)
app.MainLoop()
