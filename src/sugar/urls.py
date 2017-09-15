# -*- coding: utf-8 -*-
#
from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^(?P<username>[^/]+)/?$', views.dashboard, name='dashboard'),
   url(r'^(?P<username>[^/]+)/reports/?$', views.reports, name='reports'),
   url(r'^$', views.index, name='index'),
]

