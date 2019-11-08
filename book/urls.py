from django.conf.urls import url
from book import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^upload',views.upload,name='upload'),
    url(r'^disply',views.disp, name='disply'),
    ]