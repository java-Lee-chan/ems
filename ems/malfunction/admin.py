from django.contrib import admin

from .models import Malfunction


# Register your models here.
@admin.register(Malfunction)
class MalfunctionAdmin(admin.ModelAdmin):
    list_display = ('equip', 'content', 'start_time', 'end_time', 'stop_time',
                    'method', 'responsible', 'duty')

