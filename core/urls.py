"""
WebPres project v1.
Generated by 'django-admin startproject' using Django 3.2.9.
By ronyman.com
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import filebrowser.views
from filebrowser.sites import site
from django.conf.urls import include, url

import apps.hello_world.views
import apps.user.views
urlpatterns = [
    # Core_urls
    path('admin/', admin.site.urls),
    path('', include('apps.hello_world.urls')),
    path('', include('apps.user.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
