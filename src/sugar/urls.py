# -*- coding: utf-8 -*-
#
from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.dashboard, name='index'),

   url(r'^reports/?$', views.reports, name='reports'),
   url(r'^reports/(?P<username>[^/]+)/?$', views.reports, name='reports-user'),
   url(r'^reports/(?P<username>[^/]+)/downloads/?$', views.downloads, name='downloads'),

   url(r'^dashboard/?$', views.dashboard, name='dashboard'),
   url(r'^dashboard/(?P<username>[^/]+)/?$', views.dashboard, name='dashboard-user'),
]
