from django.contrib.auth.models import User
from django.db import models
from equipment.models import Equipment


# Create your models here.
class Malfunction(models.Model):
    DUTY_1S = 0
    DUTY_2S = 1
    DUTY_ITEMS = (
        (DUTY_1S, '1S'),
        (DUTY_2S, '2S')
    )
    equip = models.ForeignKey(Equipment, verbose_name="设备名称")
    content = models.CharField(max_length=50, verbose_name="故障内容")
    start_time = models.DateTimeField(verbose_name="开始时间")
    end_time = models.DateTimeField(verbose_name="结束时间")
    stop_time = models.DateTimeField(verbose_name="故障时间")
    method = models.TextField(max_length=100, verbose_name="处理方法")
    responsible = models.ForeignKey(User, verbose_name="负责人")
    duty = models.PositiveIntegerField(default=DUTY_1S,
                                       choices=DUTY_ITEMS, verbose_name="勤务")

    class Meta:
        verbose_name = verbose_name_plural = '故障履历'

