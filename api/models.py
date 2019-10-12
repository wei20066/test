from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100) #姓名
    cardid = models.CharField(max_length=64) #卡流水号 
    timeframe = models.IntegerField() # 时段 
    email = models.EmailField() # 邮箱 
    authority = models.BooleanField() # 权限状态 
    create_time = models.DateTimeField(auto_now=True) # 创建时间（自动获取当前时间）
    class Meta:
        unique_together = ("name", "cardid")
    def __str__(self):
        return self.name

class Device(models.Model):
    number=models.IntegerField() #机号
    macaddress=models.CharField(max_length=12) #MAC地址
    type=models.IntegerField()  #设备类型
    authnumber=models.IntegerField() #权限数
    recordnumber=models.IntegerField() #未采集记录数
    workmode=models.IntegerField() #工作模式
    onlinestatus=models.IntegerField() #在线状态
    class Meta:
        unique_together = ("number", "macaddress")
    
    def __str__(self):
        return self.macaddress