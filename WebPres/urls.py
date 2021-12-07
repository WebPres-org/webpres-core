"""
WebPres project v1.
Generated by 'django-admin startproject' using Django 3.2.9.
By ronyman.com
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


import apps.hello_world.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", apps.hello_world.views.home, name="home"),
    path("new", apps.hello_world.views.new, name="new"),
    #path('', include('apps.hello_world.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
