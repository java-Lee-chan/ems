from django.contrib.auth.models import User
from django.db import models
from equipment.models import Equipment


# Create your models here.
class Accessory(models.Model):
    equip = models.ForeignKey(Equipment, verbose_name="设备名称")
    name = models.CharField(max_length=50, verbose_name="备件名称")
    model = models.CharField(max_length=50, verbose_name="备件型号")
    type = models.CharField(max_length=50, verbose_name="备件规格")
    quantity = models.IntegerField(verbose_name="备件数量")
    price = models.DecimalField(max_digits=6, decimal_places=1, verbose_name="备件价格")
    position = models.CharField(max_length=50, verbose_name="备件位置")
    purchaser = models.ForeignKey(User, verbose_name="采购人")

    class Meta:
        verbose_name = verbose_name_plural = '备件管理'

    def __str__(self):
        return self.name
