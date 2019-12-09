#coding:utf-8
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event,Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from sign.models import Pictures
from django.urls import reverse
from uuid import uuid4
import os
from django import forms
import datetime

# Create your views here.
def index(request):
    return render(request,"index.html")
    
def login(request):
    return render(request,"login.html")

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user) # 登录 
            request.session['user'] = username # 将session信息记录到浏览器 
            response = HttpResponseRedirect('/event_manage/')
            return response 
        else:
            return render(request,'index.html', {'error': 'username or password error!'})
        '''
        if username == 'admin' and password == 'admin123':
           response = HttpResponseRedirect('/event_manage/') 
           #response.set_cookie('user', username, 3600)
           request.session['user']=username # 将 session 信息记录到浏览器

           return response 
        #return HttpResponseRedirect('/event_manage/')
        #return HttpResponse('login success!')            
        else:
            return render(request,'index.html', {'error': 'username or password error!'})
    else:
        return render(request,'index.html', {'error': 'username or password error!'})
'''
'''
@login_required 
def event_manage(request):
    event_list = Event.objects.all()
    username = request.session.get('user', '')
    return render(request,"event_manage.html",{"user": username, "events":event_list})
'''

@login_required
def event_manage(request):
    username = request.session.get('user', '')
    event_list = Event.objects.all()
    paginator = Paginator(event_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page. 
        contacts = paginator.page(1) 
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results. 
        contacts = paginator.page(paginator.num_pages)
    return render(request, "event_manage.html", {"user": username, "events": contacts})

@login_required 
def search_guest_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get("name", "")
    guest_list = Guest.objects.filter(realname__contains=search_name)
    return render(request, "guest_manage.html", {"user": username, "guests": guest_list})
    
@login_required 
def search_event_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get("name", "")
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request, "event_manage.html", {"user": username, "events": event_list})
    
'''
@login_required 
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    return render(request, "guest_manage.html", {"user": username, "guests": guest_list}) 
'''    
@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list, 4)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page. 
        contacts = paginator.page(1) 
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results. 
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user": username, "guests": contacts})

# 签到页面 
@login_required
def sign_index(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'sign_index.html', {'event': event})
    
# 签到动作 
@login_required 
def sign_index_action(request,event_id):
    event = get_object_or_404(Event, id=event_id)
    phone = request.POST.get('phone','')
    result = Guest.objects.filter(phone = phone)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': 'phone error.'})
    result = Guest.objects.filter(phone=phone,event_id=event_id)
    if not result: 
        return render(request, 'sign_index.html', {'event': event, 'hint':'event id or phone error.'})
    result = Guest.objects.get(phone=phone,event_id=event_id)
    if result.sign:
        return render(request, 'sign_index.html', {'event': event, 'hint': "user has sign in."})
    else: 
        Guest.objects.filter(phone=phone,event_id=event_id).update(sign = '1')
        return render(request, 'sign_index.html', {'event': event, 'hint':'sign in success!','guest': result})

# 退出登录 
@login_required 
def logout(request):
    auth.logout(request) #退出登录
    response = HttpResponseRedirect('/accounts/login/')
    return response


class PictureForm(forms.Form):
    title=forms.CharField()
    headImg=forms.FileField()

# 上传图片
# 返回上传图片的页面
def get_upload_form(request):
    if request.method=="POST":
        pcf=PictureForm(request.POST)
        if pcf.is_valid():
            print(pcf.cleaned_data['title'])
            return HttpResponse('OK')
    else:
        pcf=PictureForm()
    return render(request,'upload_image.html',{'pcf':pcf})
    #return render(request,'upload_image.html')

#　发来表单　实现上传功能
def upload(request):
    # 从请求当中　获取文件对象
    f1 = request.FILES.get('headImg')
    tit = request.POST.get('title','')
    filename=f1.name
    ext=filename.split('.')[-1]
    #　利用模型类　将图片要存放的路径存到数据库中
    p = Pictures()
    #ext = fl.name
    f1.name = '{}.{}'.format(uuid4().hex, ext)
    p.pic = "img/" + f1.name
    p.title=tit
    p.save()
    # 在之前配好的静态文件目录static/media/booktest 下 新建一个空文件
    # 然后我们循环把上传的图片写入到新建文件当中
    fname = settings.MEDIA_ROOT + "/img/" + f1.name
    with open(fname,'wb') as pic:
        for c in f1.chunks():
            pic.write(c)
    return HttpResponse("上传成功")
    
def get_upload_model(request):
    return render(request,'upload_image1.html')

def upload_a(request):
    # 从请求当中　获取文件对象
    f1 = request.FILES.get('picture')
    #filename=f1.name
    #ext=filename.split('.')[-1]
    #　利用模型类　将图片要存放的路径存到数据库中
    #ext = fl.name
    #f1.name = '{}.{}'.format(uuid4().hex, ext)
    # 在之前配好的静态文件目录static/media/booktest 下 新建一个空文件
    # 然后我们循环把上传的图片写入到新建文件当中
    fname = settings.MEDIA_ROOT + "/img/" + f1.name
    with open(fname,'wb') as pic:
        for c in f1.chunks():
            pic.write(c)
    return HttpResponse("上传成功")    

def show_pic(request):
   pic_obj = Pictures.objects.get(id=12)
   return render(request,'show_pic.html',{'pic_obj':pic_obj})
   
   
def hours_ahead(request,offset):
    try: 
        offset = int(offset) 
    except ValueError:
        raise Http404() 
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In %s hour(s), it will be %s. " % (offset, dt) 
    return HttpResponse(html)