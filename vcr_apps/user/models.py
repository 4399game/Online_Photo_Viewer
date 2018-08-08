# Import
# here that import Python module
import os
from django.db import models
from django.db.models import Q
from django.utils import timezone

# Import 
# here that import your module
from ..web.models import Lang
from ..vcr_conf import (kouza_path, vcr_web_path,
                        station_pic_flag, station_img_flag, 
                        def_keep_day,
                        i_middle
)

# Some globals
STATUS_CHOIES = (
    (True, '可用'),
    (None, '默认'),
    (False, '不可用'),
)
SHEN_CHOISE = (
    (True, '省流模式'),
    (False, '正常模式'),
    (None, '待机')
)
DOH_CHOISE = (
    (True, '原图模式'),
    (False, '均衡模式'),
    (None, '缩略图模式')
)
ZHE_CHOISE = (
    (True, '折叠'),
    (False, '展开'),
    (None, '隐藏')
)
LAYOUT_CHOISE = (
    ('max', '最大显示'),
    ('block', '块状布局'),
    ('grid', '栅格布局')
)
MAIN_COLOR = (
    ('teal', '水绿'),
    ('red', '红色'),
    ('yellow', '黄色'),
    ('green', '绿色'),
    ('pink', '粉色'),
    ('orange', '橙色'),
    ('blue', '蓝色'),
    ('purple', '紫色'),
    ('violet', '紫罗兰'),
    ('brown', '棕色'),
    ('grey', '灰色'),
    ('olive', '橄榄'),
)
DIY_COLOR = (
    ('rgba(255, 174, 200, ', '粉色'),
    ('rgba(0, 168, 243, ', '蓝色'),
    ('rgba(255, 242, 0, ', '黄色'),
    ('rgba(14, 209, 69, ', '绿色'),
    ('rbga(236, 28, 36, ', '红色'),
    ('rgba(140, 255, 251, ', '水绿'),
    ('rgba(255, 202, 24, ', '金色'),
    ('rgba(196, 255, 14, ', '浅绿'),
    ('rgba(255, 127, 39, ', '橙色'),
    ('rgba(63, 72, 204, ', '靛蓝'),
    ('rgba(185, 122, 86, ', '褐色'),
    ('rgba(253, 236, 166, ', '浅黄'),
    ('rgba(136, 0, 27, ', '深红'),
    ('rgba(184, 61, 186, ', '紫色'),
    ('rgba(88, 88, 88, ', '灰色'),
    ('rgba(195, 195, 195, ', '浅灰'),
)
SAFE_CHOISE = (
    (True, '安全'),
    (False, '不安全'),
    (None, '未知'),
)
JM = (
    ('[1]', '回收站'),
    ('[2]', '个性化'),
    ('[3]', '个人中心'),
    ('[4]', '安全性'),
    ('[5]', '设置'),
    ('[6]', '全局搜索'),
    ('[4,5]', '安全性, 设置'),
    ('[1,2,3,4,5,6]', '全部'),
)
AUTHNUM_CHOIES = (
    (0, '特殊身份'),
    (1, '未知'),
    (2, '新手'),
    (3, '老用户'),
    (4, '尊贵身份'),
)
def_pwd = 'None'
def_web_name = 'VcrT'

# Create your models here.
"""
    安全
"""
class Safe(models.Model):
    kuuk_pwd = models.CharField(default = def_pwd, max_length = 247, verbose_name = '空间密码')
    ctrl_pwd = models.CharField(default = def_pwd, max_length = 247, verbose_name = '功能控制密码')
    is_tell = models.NullBooleanField(default = False, choices = SAFE_CHOISE, verbose_name = '号码是否已验证')
    is_mail = models.NullBooleanField(default = False, choices = SAFE_CHOISE, verbose_name = '邮箱是否已验证')
    which_jm = models.SmallIntegerField(default = '1_2_3_4_5_6', null = True, blank = True, verbose_name = '哪些需要加密')
    
    manager_one = models.Manager()
    def __str__(self):
        return '安全性'

class SafeAsk(models.Model):
    question = models.CharField(default = '你最喜欢谁，虚拟 or 现实的人物当中？', max_length = 247, verbose_name = '问题')
    answer = models.CharField(default = '这是我的秘密', max_length = 123, verbose_name = '答案' )

    status = models.NullBooleanField(default = True, choices = STATUS_CHOIES, verbose_name = '状态')
    safe = models.ForeignKey(Safe, on_delete = models.SET_NULL, null = True, blank = True, verbose_name = '安全性为')

    manager_one = models.Manager()
    def __str__(self):
        return '密保问题'

"""
    设置
"""
class Setting(models.Model):
    is_shen = models.NullBooleanField(default = False, choices = SHEN_CHOISE, verbose_name = '是否开启省流模式')
    is_doh = models.NullBooleanField(default = True, choices = DOH_CHOISE, verbose_name = '是否开启高质量下载模式')
    comp_ro = models.SmallIntegerField(default = i_middle, verbose_name = '压缩阈值')
    is_zhe = models.BooleanField(default = False, choices = ZHE_CHOISE, verbose_name = '是否折叠底部')
    def_layout = models.CharField(default = 'grid', max_length = 60, choices = LAYOUT_CHOISE, verbose_name = '默认布局模式')

    manager_one = models.Manager()
    def __str__(self):
        return '设置'

"""
    样式
"""
def upload_to_vcr(style, file_name):
    return os.path.join(vcr_web_path, 'bg_img', file_name)

class Style(models.Model):
    main_color = models.CharField(default = 'pink', max_length = 30, choices = MAIN_COLOR, verbose_name = '主题颜色')
    diy_color = models.CharField(default = 'rgba(255, 174, 200, ', max_length = 60, choices = DIY_COLOR, verbose_name = '样式颜色')
    
    name = models.CharField(default = def_web_name, max_length=120, verbose_name='网站名称')
    bg_img = models.ImageField(upload_to = upload_to_vcr, verbose_name='网站背景', default='def_face.jpg')

    manager_one = models.Manager()
    def __str__(self):
        return '样式'

"""
    网站控制
"""
class KouZaCtrl(models.Model):
    
    def_kuukann = models.CharField(max_length=247 ,null=True, blank=True, verbose_name='默认空间')
    lang = models.CharField(max_length=60, null=True, blank=True, verbose_name='语言')
    keep_day = models.SmallIntegerField(default=def_keep_day, verbose_name='回收站保留天数')
    layout = models.CharField(max_length=60, null=True, blank=True, verbose_name='排列方式')
    auth_num = models.SmallIntegerField(default = '0', choices = AUTHNUM_CHOIES, verbose_name='账号身份')

    create_date = models.DateTimeField(default=timezone.now(), verbose_name='创建时间')
    update_date = models.DateTimeField(default = timezone.now(), verbose_name='最近更新时间')

    manager_one = models.Manager()
    def __str__(self):
        return '网站控制'

"""
    用户
"""
def upload_to_kouza(kouza, file_name):
    return os.path.join(kouza_path, str(kouza.create_date).replace(':', '_').replace('：', '_'), 'face', file_name)

class KouZaManager(models.Manager):
    def get_queryset(self):
        return super(KouZaManager, self).get_queryset().filter(status = True)

class KouZa(models.Model):
    last_name = models.CharField(max_length = 60, verbose_name = '姓')
    first_name = models.CharField(max_length = 123, verbose_name = '名')

    name = models.CharField(max_length = 247, verbose_name = '姓名')

    email = models.EmailField(null = True, blank = True, verbose_name = '邮箱')
    phone = models.CharField(max_length = 60, null = True, blank = True, verbose_name = '电话')
    face = models.ImageField(upload_to = upload_to_kouza, verbose_name = '用户头像', default = 'def_face.jpg')
    status = models.NullBooleanField(default=True, choices = STATUS_CHOIES, verbose_name='状态')

    safe = models.ForeignKey(Safe, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属安全性')
    style = models.ForeignKey(Style, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属个性化')
    setting = models.ForeignKey(Setting, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属设置')
    kouza_ctrl = models.ForeignKey(KouZaCtrl, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属网站配置')

    create_date = models.DateTimeField(default = timezone.now(), verbose_name='创建时间')
    
    manager_one = models.Manager()
    manager_two = KouZaManager()
    def __str__(self):
        return self.name

    # 获取 回收站 失效相册 的数量
    def get_station_pic_count(self):
        return self.station_set.filter(Q(status = True) & Q(station_flag = station_pic_flag)).count()

    # 获取 回收站 失效图片 的数量
    def get_station_img_count(self):
        return self.station_set.filter(Q(status = True) & Q(station_flag = station_img_flag)).count()

