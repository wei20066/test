from django.shortcuts import render
from django.http import JsonResponse 
from django.core.exceptions import ValidationError,ObjectDoesNotExist
from django.db.utils import IntegrityError 
import time 
import json
import binascii

# Create your views here.
def heartBeatApi1(request):
    postBody=request.body
    json_result = json.loads(postBody)      
    return JsonResponse(json_result)
    
def heartBeatApi(request):
    postBody=request.body
    json_result = json.loads(postBody)
    if json_result['content']:
       if json_result['content'][18:20]=='00':
            mac=json_result['content'][0:12]
            devtype=json_result['content'][12:14]
            hexdevnu=json_result['content'][14:20]
            devnu=json_result['content'][18:20]+json_result['content'][16:18]+json_result['content'][14:16]
            devnu=str(int("0x" +devnu,16))
            devnum=json_result['content'][14:18]
            
            print("[设备心跳包]>>>"+json_result['content'])
            print('设备MAC:'+mac+' 设备类型:'+devtype+' 设备号:'+devnu)
            json_result['content']=mac+hexdevnu+time.strftime("%y%m%d%H%M%S")+'01'
            print("[服务器回包]>>>"+json_result['content'])
            return JsonResponse(json_result)
    else:
        return JsonResponse({'status':10024,'message':error})
    if json_result['access']:
        print(json_result['access'])
    if json_result['instruct']:
        print(json_result['instruct'])         
    return JsonResponse(json_result)
    
def onlineAccessApi(request):
    postBody=request.body
    json_result = json.loads(postBody)
    if json_result['content']:
       if json_result['content'][22:24]=='A1':
            mac=json_result['content'][8:20]
            devtype=json_result['content'][20:22]
            statuscode=json_result['content'][24:28]
            waternum=json_result['content'][28:34]
            print("通讯流水号"+waternum)
            readerid=json_result['content'][34:35]
            #cardid=json_result['content'][34:42]
            #print(cardid)
            cardid=int('0x'+json_result['content'][40:42]+json_result['content'][38:40]+json_result['content'][36:38]+json_result['content'][34:36],16)
            print("[联网鉴权包]>>>"+json_result['content'])
            print('设备MAC:'+mac+' 设备类型:'+devtype+' 状态码:'+statuscode+' 读头号:'+readerid+' 卡流水号:'+ str(cardid))
            json_result['content']='55BB4000'+mac+devtype+'A1A005000000'+'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF1E55EE'
            print("[服务器回包]>>>"+json_result['content'])
            print("无权限")
            json_result['content']='55BB4000'+mac+devtype+'A19000000000'+str(cardid)
            return JsonResponse(json_result)
    else:
        return JsonResponse({'status':10024,'message':error})
      

def accessApi(request): 
    postBody=request.body
    json_result = json.loads(postBody)
    #print(json_result['access'][22:24])
    if json_result['access']:
        if json_result['access'][22:24]=='A4':
            commad=json_result['access'][22:24]
            macadrr=json_result['access'][8:20]
            print('MAC地址 '+macadrr)
            type=json_result['access'][20:22]
            print('设备类型 '+ type)
            statuscode=json_result['access'][24:28]
            print('状态码 '+ statuscode)
            waternum=json_result['access'][28:34]
            print('通讯流水号 '+ waternum)
            #print(json_result['access'][40:42]+json_result['access'][38:40]+json_result['access'][36:38]+json_result['access'][34:36])
            cardid=int('0x'+json_result['access'][40:42]+json_result['access'][38:40]+json_result['access'][36:38]+json_result['access'][34:36],16)
            shiduan=json_result['access'][42:46]
            name=json_result['access'][46:78]
            name=binascii.a2b_hex(name)
            authoritybit=json_result['access'][78:82]
            print('权限位'+authoritybit)
            #name=name.decode('gbk').encode('utf-8')
            name=name.decode('gbk')
            print(name)           
            print(cardid)
            power=json_result['access'][78:82]
            
            json_result['content']=''
            json_result['access']='55BB0F00'+macadrr+type+commad+'9000'+waternum+'009555EE'
            json_result['instruct']=''
             
        return JsonResponse(json_result)
    