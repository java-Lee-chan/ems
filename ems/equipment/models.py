from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Zone(models.Model):
    name = models.CharField(max_length=50, verbose_name="区域名称")

    class Meta:
        verbose_name = verbose_name_plural = '设备区域'

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=50, verbose_name="设备名称")
    zone = models.ForeignKey(Zone, verbose_name="所属区域")
    attribute = models.TextField(verbose_name="属性")
    owner = models.ForeignKey(User, verbose_name="负责人")

    class Meta:
        verbose_name = verbose_name_plural = '设备管理'

    def __str__(self):
        return self.name

    @classmethod
    def get_row(cls):
        row = []
        first_row = ['', 'name', 'zone', 'attribute', 'owner']
        row.append(first_row)
        equip = cls.objects.all()
        for i in range(len(equip)):
            row.append([i+1, equip[i].name, equip[i].zone, equip[i].attribute, equip[i].owner])
        return row



