# Import
# here that import Python module
from django.db import models
from django.utils import timezone

# Import 
# here that import your module
from ..user.models import KouZa
from ..kuukann.models import Pic, Img

# Globel
STATION_CHOIES = (
    (True, '项目在回收站中'),
    (None, '项目已被抛弃'),
    (False, '项目已被还原'),
)

# Create your models here.
class StationManager(models.Manager):
    def get_queryset(self):
        return super(StationManager, self).get_queryset().filter(status = False)

class Station(models.Model):
    kouza = models.ForeignKey(KouZa, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属用户')
    pic = models.ForeignKey(Pic, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属相册')
    img = models.ForeignKey(Img, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属图片')
    
    station_flag = models.CharField(max_length=30, verbose_name='回收标志')
    false_date = models.DateTimeField(default=timezone.now(), verbose_name='放入时间')
    unshow_date = models.DateTimeField(null=True, blank=True, verbose_name='不显示时间')
    status = models.NullBooleanField(choices=STATION_CHOIES, default=True, verbose_name='数据状态')
    
    manager_one = models.Manager()
    manager_two = StationManager()

    def __str__(self):
        return self.kouza.name+ '的回收数据'
