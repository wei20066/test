import wx

class Toneplus(wx.Frame):
	def __init__(self,parent=None):
		wx.Frame.__init__(self, parent, -1, 'Test Tool', size=(600, 300))
		panel = wx.Panel(self)
		sizer = wx.BoxSizer(wx.VERTICAL)
		panel.SetSizer(sizer)
		self.ip_stctxt=wx.StaticText(panel, -1, u'ip地址：', (20,20), (60, 20))
		self.ip_tbox=wx.TextCtrl(panel, -1, u'*', (80, 18), (80, 20))
		self.Port_stctxt=wx.StaticText(panel, -1, u'端口：', (164, 20), (40, 20))
		self.prot_tbox=wx.TextCtrl(panel,-1,u'*',(204,18),(40,20))
		self.start_btn=wx.Button(panel, -1, u'运行', pos=(248, 18))
		self.Bind(wx.EVT_BUTTON,self.onStart,self.start_btn)

	def onStart(self,event):
		print("running.......")

class MyApp(wx.App):  # 自定义应用程序对象

    def OnInit(self):
        #print ("MyApp OnInit")
        self.frame = Toneplus(None)
        id = self.frame.GetId()
        print ("Frame ID:", id)
        self.frame.Show(True)
        return True

if __name__ == '__main__':
    app = MyApp()  # 使用从wx.App继承的子类
    app.MainLoop()