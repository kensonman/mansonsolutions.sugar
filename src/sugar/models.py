# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _
from webframe.models import ValueObject


class Record(ValueObject):
   class Meta(object):
      verbose_name            = _('Record')
      verbose_name_plural     = _('Records')

   owner                      = models.ForeignKey(get_user_model(), verbose_name=_('Record.owner'))
   sugar                      = models.FloatField(default=0,verbose_name=_('Record.sugar'))
   pulse                      = models.IntegerField(default=0,verbose_name=_('Record.pulse'))
   sys                        = models.IntegerField(default=0,verbose_name=_('Record.sys'))
   dia                        = models.IntegerField(default=0,verbose_name=_('Record.dia'))

