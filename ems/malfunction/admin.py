from django.contrib import admin

from .models import Malfunction


# Register your models here.
@admin.register(Malfunction)
class MalfunctionAdmin(admin.ModelAdmin):
    list_display = ('equip', 'content', 'start_time', 'end_time', 'stop_time',
                    'method', 'responsible', 'duty')

    fields = ('equip', 'content', 'start_time', 'end_time',
              'method', 'responsible', 'duty')

    def save_model(self, request, obj, form, change):
        obj.stop_time = obj.end_time - obj.start_time
        return super(MalfunctionAdmin, self).save_model(request, obj, form, change)
