from django.conf.urls import url

from devlibrary.views import libraries_list, library, librarydetail

urlpatterns = [
    url(r'^$', libraries_list, name='devlibrary'),
    url(r'^(?P<id>\d+)/$', librarydetail, name='devsdetail'),
]
