from django.conf.urls import url
from book import views

urlpatterns = [
    url(r'^book/index/', views.index,name='index'),
    ]