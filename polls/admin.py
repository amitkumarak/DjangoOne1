from django.contrib import admin

from polls.models import Images

from polls.models import post

# Register your models here.

admin.site.register(post)

admin.site.register(Images)
