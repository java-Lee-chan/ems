from django.contrib import admin

from .models import Maintenance


# Register your models here.
@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('equip', 'area', 'name', 'method', 'target', 'type', 'period', 
                    'next_time', 'guide', 'owner', 'result')
    fields = ('equip', 'area', 'name', 'method', 'target', 'type', 'period', 'start_time', 'guide', 'owner', 'result')

    def save_model(self, request, obj, form, change):
        obj.next_time = obj.start_time
        return super(MaintenanceAdmin, self).save_model(request, obj, form, change)
