from django.contrib import admin
from .models import Record

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
   list_display=('owner', 'sugar', 'pulse', 'sys', 'dia', 'lmb', 'lmd')
