from django.contrib import admin

from .models import Equipment, Zone


# Register your models here.
@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'zone', 'attribute', 'owner')
    fields = ('name', 'zone', 'attribute', 'owner')


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    fields = ('name',)

