from django.contrib.auth.models import User
from django.db import models
from equipment.models import Equipment


# Create your models here.
class Maintenance(models.Model):
    PERIOD_EVERYDAY = 0
    PERIOD_EVERYMONTH = 1
    PERIOD_THIRDMONTH = 2
    PERIOD_HALFYEAR = 3
    PERIOD_EVERYYEAR = 4
    PEROID_THIRDYEAR = 5
    PERIOD_ITEMS = (
        (PERIOD_EVERYDAY, '每日'),
        (PERIOD_EVERYMONTH, '１个月'),
        (PERIOD_THIRDMONTH, '３个月'),
        (PERIOD_HALFYEAR, '６个月'),
        (PERIOD_EVERYYEAR, '１年'),
        (PEROID_THIRDYEAR, '３年'),
    )

    equip = models.ForeignKey(Equipment, verbose_name="设备名称")
    area = models.CharField(max_length=50, verbose_name="设备部位")
    name = models.CharField(max_length=100, verbose_name="项目名称")
    method = models.CharField(max_length=50, verbose_name="检查方式")
    target = models.TextField(max_length=100, verbose_name="点检标准")
    type = models.CharField(max_length=50, verbose_name="领域")
    period = models.PositiveIntegerField(default=PERIOD_EVERYDAY,
                                         choices=PERIOD_ITEMS, verbose_name="周期")
    start_time = models.DateTimeField(verbose_name="开始时间")
    next_time = models.DateTimeField(verbose_name="下次时间")
    guide = models.FileField(verbose_name="指导书")
    owner = models.ForeignKey(User, verbose_name="负责人")
    result = models.CharField(max_length=50, verbose_name="结果")

    class Meta:
        verbose_name = verbose_name_plural = '点检保养'

    def __str__(self):
        return self.name


