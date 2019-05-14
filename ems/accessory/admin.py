from django.contrib import admin

from .models import Accessory


# Register your models here.
@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'type', 'quantity', 'price', 'position', 'purchaser')