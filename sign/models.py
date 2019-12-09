from django.db import models
from datetime import date
# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100) # 发布会标题
    limit = models.IntegerField() # 参加人数 
    status = models.BooleanField() # 状态 
    address = models.CharField(max_length=200) # 地址 
    start_time = models.DateTimeField('events time') # 发布会时间 
    create_time = models.DateTimeField(auto_now=True) # 创建时间（自动获取当前时间）

    def __str__(self):
        return self.name# 嘉宾表
    class Meta:
        ordering=['name']

class Guest(models.Model):
    event = models.ForeignKey(Event) # 关联发布会id 
    realname = models.CharField(max_length=64) # 姓名 
    phone = models.CharField(max_length=16) # 手机号 
    email = models.EmailField() # 邮箱 
    sign = models.BooleanField() # 签到状态
    photo=models.CharField(max_length=100) #照片存放路径
    #img = models.ImageField(upload_to='img',null=True)
    create_time = models.DateTimeField(auto_now=True) # 创建时间（自动获取当前时间）
    class Meta:
        unique_together = ("event", "phone")
    def __str__(self):
        return self.realname


class Pictures(models.Model):
    title = models.CharField("标题", max_length=100, blank=True, default='')
    pic = models.ImageField("图片",upload_to='img/',blank=True)
    date = models.DateField(default=date.today)
    def __str__(self):
        return self.pic
        
class Users(models.Model):
    name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='img',null=True)
    def __str__(self):
        return self.name

class tasks(models.Model):
    title=models.CharField(max_length=128)
    issue=models.CharField(max_length=512)
    create_date=models.DateTimeField(auto_now=True)
    close_date=models.DateTimeField()
    status=models.BooleanField()
    def __str__(self):
        return self.title
    class Meta: 
        ordering = ['title']