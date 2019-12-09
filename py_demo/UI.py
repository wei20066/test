#coding:utf8
import time
import threading
import wx
import serial

class MyFrame(wx.Frame):
	
	def __init__(self,parent):
		print("MyFrame __init__") 
		wx.Frame.__init__(self,parent,-1,'My COM',size=(500,500))#窗口标题栏和大小         
		panel=wx.Panel(self)        
		sizer=wx.BoxSizer(wx.VERTICAL)        
		panel.SetSizer(sizer)         
		self.sendtxt=wx.StaticText(panel,-1,u'发送',(20,50),(50,15))#发送静态文本框         
		self.rectxt=wx.StaticText(panel,-1,u'接收',(20,200),(50,15))#接收静态文本框        
		self.baudratetxt=wx.StaticText(panel,-1,u'波特率',(20,320),(50,15))#波特率静态文本框        
		self.comtxt=wx.StaticText(panel,-1,'com',(20,350),(50,15))#com口静态文本框        
		baudratelist=['300','600','1200','2400','4800','9600','19200','38400'                     
		,'43000','56000','57600','115200']        
		comlist=['com1','com2','com3','com4','com5','com6','com7','com8','com9']         
		self.baudratelistctr=wx.Choice(panel, -1, (70, 320), choices=baudratelist)        
		self.Bind(wx.EVT_CHOICE,self.OnbaudrateCH,self.baudratelistctr)#波特率下拉列表响应函数        
		self.comlistctr=wx.Choice(panel, -1, (70, 350), choices=comlist)        
		self.Bind(wx.EVT_CHOICE,self.OncomlistCH,self.comlistctr)#com下拉列表响应函数        
		self.baudratelistctr.SetSelection(5)        
		self.comlistctr.SetSelection(3)
		self.sendctr = wx.TextCtrl(panel, -1,                                  
		pos = (100, 50), size = (200, 100),                    
		style=wx.TE_MULTILINE|wx.TE_CENTER)        
		self.recctr = wx.TextCtrl(panel, -1,                                  
		pos = (100, 200), size = (200, 100),                    
		style=wx.TE_MULTILINE|wx.TE_CENTER)                
		self.sendbutton=wx.Button(panel,-1,u'发送',pos=(350,50))#发送按钮        
		self.Bind(wx.EVT_BUTTON,self.OnSend,self.sendbutton)        
		self.ClearRecbutton=wx.Button(panel,-1,u'清空接收列表',pos=(350,200))        
		self.Bind(wx.EVT_BUTTON,self.OnClearRec,self.ClearRecbutton)               
		index=self.baudratelistctr.GetSelection()        
		BaudRate=self.baudratelistctr.GetString(index)#获取波特率        
		index=self.comlistctr.GetSelection()        
		ComNum=self.comlistctr.GetString(index)#获取com口 
		t = threading.Timer(0.1,self.myreceive)        
		t.start()        
		self.Centre()        
		global mycom                
		try:              
			mycom= serial.Serial(ComNum,BaudRate,timeout=1)                        
		except:            
			wx.MessageBox('open com fail','error')            
		return None                    
	
	def myreceive(self):
		try:
			n=mycom.inWaiting()
		except:
			return None
		if n!=0:
			str1=mycom.read(n)
			self.recctr.Value=str1
			t = threading.Timer(0.1,self.myreceive)
			t.start()    

	def OnClearRec(self,event):
		        self.recctr.Value=''
		
	def OnbaudrateCH(self,event):       
		 global mycom        
		 index=self.baudratelistctr.GetSelection()        
		 BaudRate=self.baudratelistctr.GetString(index)#获取波特率        
		 mycom.setBaudrate(BaudRate)        
		 print(mycom.inWaiting )                   

	def OncomlistCH(self,event):
		global mycom        
		index=self.comlistctr.GetSelection()        
		ComNum=self.comlistctr.GetString(index)#获取com口                
		try:
			mycom.setPort(ComNum)        
		except:
		    wx.MessageBox('change port fail','error')            
		return None       
		print(mycom.inWaiting)
	
	def OnSend(self,event):                    #发送处理程序
		value=self.sendctr.GetValue()
		n=mycom.write(value)       
'''    	    
	    def OnRec(self,event):                     #接收处理程序        
	    	n=mycom.inWaiting()        
	    	str1=mycom.read(n)        
	    	self.recctr.Value=str1 
'''    
		

class MyApp(wx.App): #自定义应用程序对象     
	
	def OnInit(self):
		print ("MyApp OnInit")
		self.frame = MyFrame(None)
		id=self.frame.GetId()
		print ("Frame ID:",id)
		self.frame.Show(True)
		return True    

	def OnExit(self):        
	    print ("MyApp OnExit")
	    mycom.close()
	    time.sleep(2)         

if __name__ == '__main__':
     print ("Main start")
     app = MyApp() #使用从wx.App继承的子类 
     print ("Before MainLoop")
     app.MainLoop()
     print ("After MainLoop")