from django.conf.urls import url
from api import views_if
from api import t1plusviews

urlpatterns = [
    url(r'^portal',t1plusviews.index,name='t1'), 
    # guest system interface:
    url(r'^services/hwd/consume/heartBeatApi', views_if.heartBeatApi, name='heartBeatApi'),
    url(r'^services/hwd/y2/heartBeatApi',views_if.heartBeatApi1, name='heartBeatApi1'),
    #url(r'^services/hwd/consume/onlineAccessApi',views_if.xfonlineAccessApi,name='onlineAccessApi'),
    #url(r'^services/hwd/consume/realTimeApi',views_if.xfrealTimeApi,name='realTimeApi'), 
    #url(r'^services/hwd/consume/uploadingApi',views_if.xfuploadingApi,name='uploadingApi'),
    #url(r'^services/hwd/consume/instructApi',views_if.xfinstructApi,name='instructApi'),
    # ex : /api/get_event_list/ 
    url(r'^services/hwd/TPlus/onlineAccessApi',views_if.onlineAccessApi,name='onlineAccessApi'),
    url(r'^services/hwd/TPlus/heartBeatApi',views_if.heartBeatApi,name='heartBeatApi'),
    #url(r'^services/hwd/TPlus/instructApi',views_if.instructApi,name='instructApi'),
    #url(r'^services/hwd/TPlus/realTimeApi',views_if.mjrealTimeApi,name='realTimeApi'),
    #url(r'^services/hwd/TPlus/uploadingApi',views_if.mjuploadingApi,name='uploadingApi'),
    #url(r'^services/hwd/TPlus/statusDevApi',views_if.mjstatusDevApi,name='statusDevApi'),
    url(r'^services/hwd/TPlus/accessApi',views_if.accessApi,name='accessApi'),
    #url(r'^get_event_list/', views_if.get_event_list, name='get_event_list'), 
    
    ]