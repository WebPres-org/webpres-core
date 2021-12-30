# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 ronyman.com
"""

from django.urls import path
from django.urls import path, include
from . import views
from .views import profile
import apps.user.views


urlpatterns = [
    #User
    path("register/", apps.user.views.register_request, name="register"),
    path("login/", apps.user.views.login_request, name="login"),
    path("myprofile/", apps.user.views.profile, name="Myprofile"),
    path('profile/', profile, name='users-profile'),
    path("logout/", apps.user.views.logout_request, name= "logout"),
    path('tinymce/', include('tinymce.urls')),
]