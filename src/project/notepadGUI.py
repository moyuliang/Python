# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"记事本", pos = wx.DefaultPosition, size = wx.Size( 809,575 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"New", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )
		
		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Open...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem2 )
		
		self.m_menuItem3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem3 )
		
		self.m_menuItem4 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Save As...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem4 )
		
		self.m_menu1.AppendSeparator()
		
		self.m_menuItem5 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Page Setup...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem5 )
		
		self.m_menuItem6 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Print...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem6 )
		
		self.m_menu1.AppendSeparator()
		
		self.m_menuItem7 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem7 )
		
		self.m_menubar1.Append( self.m_menu1, u"File" ) 
		
		self.m_menu2 = wx.Menu()
		self.m_menuItem8 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Undo", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem8 )
		
		self.m_menu2.AppendSeparator()
		
		self.m_menuItem9 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Cut", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem9 )
		
		self.m_menuItem10 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Copy", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem10 )
		
		self.m_menuItem11 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Paste", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem11 )
		
		self.m_menuItem12 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Delete", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem12 )
		
		self.m_menu2.AppendSeparator()
		
		self.m_menuItem13 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Find...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem13 )
		
		self.m_menuItem14 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Find Next", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem14 )
		
		self.m_menuItem15 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Replace", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem15 )
		
		self.m_menuItem16 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Go To...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem16 )
		
		self.m_menu2.AppendSeparator()
		
		self.m_menuItem17 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Select All", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem17 )
		
		self.m_menuItem18 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Time/Date", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem18 )
		
		self.m_menubar1.Append( self.m_menu2, u"Edit" ) 
		
		self.m_menu3 = wx.Menu()
		self.m_menuItem19 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Word Wrap", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem19 )
		
		self.m_menuItem20 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Font...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem20 )
		
		self.m_menubar1.Append( self.m_menu3, u"Format" ) 
		
		self.m_menu4 = wx.Menu()
		self.m_menuItem21 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Status Bar", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.Append( self.m_menuItem21 )
		
		self.m_menubar1.Append( self.m_menu4, u"View" ) 
		
		self.m_menu5 = wx.Menu()
		self.m_menuItem22 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"View Help", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.Append( self.m_menuItem22 )
		
		self.m_menuItem23 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"About Notepad", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.Append( self.m_menuItem23 )
		
		self.m_menubar1.Append( self.m_menu5, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		# WARNING: wxPython code generation isn't supported for this widget yet.
		self.m_scintilla1 = wx.Window( self )
		bSizer1.Add( self.m_scintilla1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.New, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.Open, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.Save, id = self.m_menuItem3.GetId() )
		self.Bind( wx.EVT_MENU, self.Save_As, id = self.m_menuItem4.GetId() )
		self.Bind( wx.EVT_MENU, self.Page_Setup, id = self.m_menuItem5.GetId() )
		self.Bind( wx.EVT_MENU, self.Print, id = self.m_menuItem6.GetId() )
		self.Bind( wx.EVT_MENU, self.Exit, id = self.m_menuItem7.GetId() )
		self.Bind( wx.EVT_MENU, self.Undo, id = self.m_menuItem8.GetId() )
		self.Bind( wx.EVT_MENU, self.Cut, id = self.m_menuItem9.GetId() )
		self.Bind( wx.EVT_MENU, self.Copy, id = self.m_menuItem10.GetId() )
		self.Bind( wx.EVT_MENU, self.Paste, id = self.m_menuItem11.GetId() )
		self.Bind( wx.EVT_MENU, self.Delete, id = self.m_menuItem12.GetId() )
		self.Bind( wx.EVT_MENU, self.Find, id = self.m_menuItem13.GetId() )
		self.Bind( wx.EVT_MENU, self.Find_Next, id = self.m_menuItem14.GetId() )
		self.Bind( wx.EVT_MENU, self.Replace, id = self.m_menuItem15.GetId() )
		self.Bind( wx.EVT_MENU, self.Go_To, id = self.m_menuItem16.GetId() )
		self.Bind( wx.EVT_MENU, self.Select_All, id = self.m_menuItem17.GetId() )
		self.Bind( wx.EVT_MENU, self.Time_Date, id = self.m_menuItem18.GetId() )
		self.Bind( wx.EVT_MENU, self.Word_Wrap, id = self.m_menuItem19.GetId() )
		self.Bind( wx.EVT_MENU, self.Font, id = self.m_menuItem20.GetId() )
		self.Bind( wx.EVT_MENU, self.Status_Bar, id = self.m_menuItem21.GetId() )
		self.Bind( wx.EVT_MENU, self.View_Help, id = self.m_menuItem22.GetId() )
		self.Bind( wx.EVT_MENU, self.About_Notepad, id = self.m_menuItem23.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def New( self, event ):
		event.Skip()
	
	def Open( self, event ):
		event.Skip()
	
	def Save( self, event ):
		event.Skip()
	
	def Save_As( self, event ):
		event.Skip()
	
	def Page_Setup( self, event ):
		event.Skip()
	
	def Print( self, event ):
		event.Skip()
	
	def Exit( self, event ):
		event.Skip()
	
	def Undo( self, event ):
		event.Skip()
	
	def Cut( self, event ):
		event.Skip()
	
	def Copy( self, event ):
		event.Skip()
	
	def Paste( self, event ):
		event.Skip()
	
	def Delete( self, event ):
		event.Skip()
	
	def Find( self, event ):
		event.Skip()
	
	def Find_Next( self, event ):
		event.Skip()
	
	def Replace( self, event ):
		event.Skip()
	
	def Go_To( self, event ):
		event.Skip()
	
	def Select_All( self, event ):
		event.Skip()
	
	def Time_Date( self, event ):
		event.Skip()
	
	def Word_Wrap( self, event ):
		event.Skip()
	
	def Font( self, event ):
		event.Skip()
	
	def Status_Bar( self, event ):
		event.Skip()
	
	def View_Help( self, event ):
		event.Skip()
	
	def About_Notepad( self, event ):
		event.Skip()
	

###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 287,190 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Designed by wuyuq\n\nemail:sui-xin-love@163.com\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer4.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer4.Add( self.m_button2, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

