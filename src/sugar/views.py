# -*- coding: utf-8 -*-
#
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404 as getObj
from webframe.functions import getDateTime, getDate
from .models import Record

import logging
logger=logging.getLogger('sugar.views')

def index(req):
   if req.user.is_authenticated():
      return redirect('dashboard', username=req.user.username)
   return render(req, 'webframe/empty.html')

@login_required
def dashboard(req, username=None):
   if username:
      if not (req.user.is_superuser or req.user.username==username):  return HttpResponseForbidden('Request Foridden')
   else:
      username=req.user.username

   if req.method=='POST':
      with transaction.atomic():
         r=Record()
         r.owner=getObj(get_user_model(), username=username)
         r.date=getDateTime(req.POST.get('date'))
         r.sugar=float(req.POST.get('sugar', '0'))
         r.pulse=int(req.POST.get('pulse', '0'))
         r.sys=int(req.POST.get('sys', '0'))
         r.dia=int(req.POST.get('dia', '0'))
         r.save()
         return redirect('reports-user', username=username) if username else redirect('reports')

   return render(req, 'sugar/dashboard.html', {})

@login_required
def reports(req, username=None):
   if username:
      if not (req.user.is_superuser or req.user.username==username):  return HttpResponseForbidden('Request Foridden')
   else:
      username=req.user.username

   params=dict()
   params['to']=getDate(req.GET.get('to', None), datetime.now())
   params['from']=getDate(req.GET.get('from', None), params['to']-timedelta(days=30))
   params['target']=Record.objects.filter(date__range=(params['from'], params['to'])).order_by('date')

   return render(req, 'sugar/reports.html', params)

@login_required
def downloads(req, username=None):
   pass
