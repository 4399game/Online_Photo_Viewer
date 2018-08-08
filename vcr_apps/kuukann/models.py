# Import
# here that import Python module

import os
from django.db import models
from django.utils import timezone

# Import 
# here that import your module
from ..user.models import KouZa
from ..vcr_conf import kouza_path

# Some globals
STATUS_CHOIES = (
    (True, '可用'),
    (None, '未知'),
    (False, '不可用'),
)
BOOL_CHOIES = (
    (True, '可用'),
    (False, '不可用'),
)
ORDER_BY_CHOIES = (
    ('create_date', '最早'),
    ('-create_date', '最新'),
)
LAYOUT_CHOIES = (
    ('max', '最大幅度显示'),
    ('block', 'Win10照片应用里的块状布局'),
    ('grid', '栅格系统均匀布局'),
)
GRID_CHOIES = (
    ('two', '每行8项'),
    ('four', '每行4项'),
    ('eight', '每行2项'),
    ('sixteen', '每行1项'),
)
IMAGE_RATIO_CHOIES = (
    (1/1 , '1 / 1'),
    (1/0.618 , '1 / 0.618'),

    (3/4 , '3 / 4'),
    (4/3 , '4 / 3'),

    (2/3 , '2 / 3'),
    (3/2 , '3 / 2'),

    (9/16 , '9 / 16'),
    (16/9 , '16 / 9'),
    
    (10/29 , '10 / 29'),
    (21/9 , '21 / 9'),
)
def_content = '- 空白 -'
# Create your models here.

"""
    空间
"""
class KuuKannManager(models.Manager):
    def get_queryset(self):
        return super(KuuKannManager, self).get_queryset().filter(status = True)

class KuuKann(models.Model):
    name = models.CharField(max_length=250, verbose_name='空间名称')
    index = models.SmallIntegerField(verbose_name='排序索引', default=0)
    mark = models.CharField(max_length=200, null=True, blank=True, verbose_name='备注')
    status = models.NullBooleanField(default=True, choices=STATUS_CHOIES, verbose_name='状态')
    create_date = models.DateTimeField(default=timezone.now(), verbose_name='创建时间')

    kouza = models.ForeignKey(KouZa, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属用户')

    class Meta:
        db_table = 'kuukann'

    manager_one = models.Manager()
    manager_two = KuuKannManager()
    def __str__(self):
        return self.name

    def get_pic_True(self):
        return self.pic_set.filter(status = True)

    # 获取 有用相册 的数量
    def get_pic_count(self):
        return self.pic_set.filter(status = True).count()

    # 获取 相册 的 起始时间
    def get_pic_first_date(self):
        try:
            return self.pic_set.filter(status = True).first().create_date
        except:
            return None

    # 获取 相册 的 最后时间
    def get_pic_last_date(self):
        try:
            return self.pic_set.filter(status = True).last().create_date
        except:
            return None

"""
    时间
"""
class TimeL(models.Model):
    t = models.DateField(verbose_name='时间序列')

    manager_one = models.Manager()
    def __str__(self):
        return str(self.t)

"""
    比例
"""
class RatioL(models.Model):
    r = models.FloatField(verbose_name='宽高比例')

    manager_one = models.Manager()
    def __str__(self):
        return str(self.r)

"""
    排布
"""
class Layout(models.Model):
    order_by = models.CharField(max_length=60, choices=ORDER_BY_CHOIES, default='create_date', verbose_name='排序名称')
    layout_name = models.CharField(max_length=60, choices=LAYOUT_CHOIES, default='grid', verbose_name='排列名称')
    diy_w = models.FloatField(default=1, verbose_name='自定义宽')
    diy_h = models.FloatField(default=1, verbose_name='自定义高')
    grid_name = models.CharField(max_length=60, choices=GRID_CHOIES, default='four', verbose_name='栅格名称')

    manager_one = models.Manager()
    def __str__(self):
        return '排列：'+ str(self.layout_name)+ '， 比例：'+ str(self.diy_w / self.diy_h)

"""
    相册
"""
def upload_to_pic(pic, file_name):
    return os.path.join(kouza_path, str(pic.kouza.id), str(pic.kuukann.id), 'cover', file_name)

class PicManager(models.Manager):
    def get_queryset(self):
        return super(PicManager, self).get_queryset().filter(status = True)

class Pic(models.Model):
    name = models.CharField(max_length=247, verbose_name='相册名称')
    image = models.ImageField(upload_to=upload_to_pic, verbose_name='相册封面')
    status = models.NullBooleanField(default=True, choices=STATUS_CHOIES, verbose_name='状态')

    create_date = models.DateTimeField(default=timezone.now(), verbose_name='创建时间')
    update_date = models.DateTimeField(default=timezone.now(), verbose_name='最近更新时间')

    layout = models.OneToOneField(Layout, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属排列')

    kuukann = models.ForeignKey(KuuKann, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属空间')
    kouza = models.ForeignKey(KouZa, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属用户')

    manager_one = models.Manager()
    manager_two = PicManager()
    def __str__(self):
        return self.name

    def get_img_count(self):
        return self.img_set.filter(status = True).count()

    def get_img_last(self):
        return self.img_set.filter(status = True).last()

    def get_img_first(self):
        return self.img_set.filter(status = True).first()

"""
    相册信息
"""
class PicMsg(models.Model):
    author = models.CharField(default='（unknow）', max_length=200, verbose_name='作者们')
    content = models.TextField(default='（nothing）', blank=True, verbose_name='相册介绍')
    down_mark = models.CharField(max_length=200, null=True, blank=True, verbose_name='下载链接')

    create_date = models.DateTimeField(default=timezone.now(), verbose_name='创建时间')

    manager_one = models.Manager()
    def __str__(self):
        return self.author
        
"""
    美图
"""
def upload_to_less_img(img, file_name):
    return os.path.join(kouza_path, str(img.pic.kouza.id), str(img.pic.kuukann.id), str(img.pic.id), 'less', file_name)
def upload_to_tiny_img(img, file_name):
    return os.path.join(kouza_path, str(img.pic.kouza.id), str(img.pic.kuukann.id), str(img.pic.id), file_name)
def upload_to_full_img(img, file_name):
    return os.path.join(kouza_path, str(img.pic.kouza.id), str(img.pic.kuukann.id), str(img.pic.id), 'full', file_name)

class ImgManager(models.Manager):
    def get_queryset(self):
        return super(ImgManager, self).get_queryset().filter(status = True)
class ImgThreeManager(models.Manager):
    def get_queryset(self):
        return super(ImgThreeManager, self).get_queryset().filter(status = False)

class Img(models.Model):
    width = models.SmallIntegerField(null=True, blank=True, verbose_name='宽')
    height = models.SmallIntegerField(null=True, blank=True, verbose_name='高')
    status = models.NullBooleanField(choices=STATUS_CHOIES , default=True, verbose_name='状态')
    create_date = models.DateTimeField(default=timezone.now(), verbose_name='创建时间')
    
    tiny_img = models.ImageField(upload_to=upload_to_tiny_img, verbose_name='美图')
    has_full = models.BooleanField(default=False, verbose_name='是否有原图')
    full_img = models.ImageField(upload_to=upload_to_full_img, default=None, null=True, blank=True, verbose_name='原图片')
    less_img = models.ImageField(upload_to=upload_to_less_img, default=None, null=True, blank=True, verbose_name='缩略图')

    kouza = models.ForeignKey(KouZa, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属用户')
    pic = models.ForeignKey(Pic, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属相册')

    manager_one = models.Manager()
    manager_two = ImgManager()
    manager_three = ImgThreeManager()
    def __str__(self):
        return '美图:%s'%self.tiny_img
    
class ImgMsg(models.Model):
    content = models.TextField(default = def_content, verbose_name = '内容')
    img = models.ForeignKey(Img, on_delete = models.SET_NULL, null=True, blank=True, verbose_name='所属美图')
    manager_one = models.Manager()
    def __str__(self):
        return '图片信息'

"""
    图片压缩信息
"""
class CompMsg(models.Model):
    name = models.CharField(max_length = 200, verbose_name = '图片名称')
    w = models.SmallIntegerField(null = True, blank = True, verbose_name = '原图宽')
    h = models.SmallIntegerField(null = True, blank = True, verbose_name = '原图高')
    px = models.IntegerField(null = True, blank = True, verbose_name = '总像素大小')
    fmt = models.CharField(max_length = 30, verbose_name = '图片格式')
    ratio = models.FloatField(verbose_name = '压缩比率')
    content = models.TextField(verbose_name = '内容')
    comp_time = models.FloatField(verbose_name = '压缩耗时(毫秒)')

    manager_one = models.Manager()
    def __str__(self):
        return self.name