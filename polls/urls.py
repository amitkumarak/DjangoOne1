from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^index/$', views.index, name="index"),
    url(r'^about/$', views.aboutteam, name="about"),
    url(r'^search/$', views.search_view, name="search"),
]
