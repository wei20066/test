"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from sign import views
from django.conf.urls import url, include 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^login_action/$', views.login_action),
    url(r'^event_manage/$', views.event_manage),
    url(r'^accounts/login/$', views.index), 
    url(r'^upload_image/$',views.get_upload_form),
    url(r'^upload_image1/$',views.get_upload_model),
    url(r'^upload/$',views.upload),
    url(r'^upload_a/$',views.upload_a),
    url(r'^show_pic/$',views.show_pic),
    url(r'^search_event_name/$', views.search_event_name),
    url(r'^search_guest_name/$', views.search_guest_name),
    url(r'^guest_manage/$', views.guest_manage),
    url(r'^sign_index/(?P<event_id>[0-9]+)/$', views.sign_index),
    url(r'^sign_index_action/(?P<event_id>[0-9]+)/$', views.sign_index_action),
    url(r'^logout/$', views.logout),
    url(r'^api/', include('api.urls', namespace="api")),
    url(r't1plus/',include('api.urls', namespace="t1")),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^book/$', include('book.urls', namespace="book")),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #如果单纯的是上传，文件并不用来显示或者读取，就不用加这个