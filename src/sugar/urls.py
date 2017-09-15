# -*- coding: utf-8 -*-
#
from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.dashboard, name='index'),
   url(r'^$', views.dashboard, name='dashboard'),
   url(r'^reports/?$', views.reports, name='reports'),

   url(r'^(?P<username>[^/]+)/?$', views.dashboard, name='user-dashboard'),
   url(r'^(?P<username>[^/]+)/reports/?$', views.reports, name='user-reports'),
]

