# coding:utf8
import wx


class Toneplus(wx.Frame):
    def __init__(self,image,parent=None):
        wx.Frame.__init__(self, parent, -1, 'T One Plus', size=(1200, 700))  # 窗口标题栏和大小
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(), temp.GetHeight()
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)
        menuBar = wx.MenuBar()
        FileMenu = wx.Menu()
        menuBar.Append(FileMenu, u"文件")
        FileMenu.Append(1000, u"打开")
        FileMenu.Append(1001, u"新建")
        FileMenu.AppendSeparator()
        FileMenu.Append(1002, u"保存")
        self.Bind(wx.EVT_MENU, self.OnOpen, id=1000)
        self.Bind(wx.EVT_MENU, self.OnNew, id=1001)
        self.Bind(wx.EVT_MENU, self.OnSave, id=1002)
        MenuHelp = wx.Menu()
        aboutMenu = MenuHelp.Append(-1,u"&A 关于")
        menuBar.Append(MenuHelp,u"帮助")
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_TOOL,self.ShowAboutDlg,aboutMenu)


    def OnOpen(self, event):
        wx.MessageBox("打开文件")

    def OnNew(self, event):
        wx.MessageBox("新建文件")

    def OnSave(self, event):
        wx.MessageBox("保存文件")

    def ShowAboutDlg(self,event):
        pos = self.GetPosition()
        dialog = MyDialog(self,-1,u"关于")
        dialog.SetPosition((pos[0]+100,pos[1]+60))
        dialog.ShowModal()

   

class MyApp(wx.App):  # 自定义应用程序对象
    def OnInit(self):
        #print ("MyApp OnInit")
        image = wx.Image('wxPython.jpg', wx.BITMAP_TYPE_JPEG)
        self.frame = Toneplus(image)
        id = self.frame.GetId()
        #print ("Frame ID:", id)
        self.frame.Show(True)
        return True

    def OnExit(self):
        import time
        time.sleep(2)
        return 0  # 返回状态码



if __name__ == '__main__':
    app = MyApp()  # 使用从wx.App继承的子类
    app.MainLoop()