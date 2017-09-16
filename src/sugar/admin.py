from django.contrib import admin
from .models import Record

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
   list_display=('id', 'owner', 'date', 'sugar', 'pulse', 'sys', 'dia', 'lmb', 'lmd')
