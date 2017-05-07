from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.home, name="home"),
    url(r'^index/$', views.index, name="index"),
    url(r'^about/$', views.aboutteam, name="about"),
]
