# Import
# here that import Python module

from django.db import models

# Import 
# here that import your module

"""
    颜色
"""
class Color(models.Model):
    main_val = models.CharField(max_length=30, verbose_name='颜色名称')
    diy_val = models.CharField(max_length=60, verbose_name='颜色值')

    manager_one = models.Manager()
    def __str__(self):
        return self.main_val

"""
    语言
"""
class Lang(models.Model):
    lang = models.CharField(max_length=120, verbose_name='语言名称')

    manager_one = models.Manager()
    def __str__(self):
        return self.lang

"""
    语言文字
"""
class Text(models.Model):
    page = models.CharField(max_length=120, verbose_name='页面标识')
    flag = models.CharField(max_length=120, verbose_name='文字标识')
    content = models.TextField(verbose_name='具体内容')

    lang = models.ForeignKey(Lang, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属语言')

    manager_one = models.Manager()
    def __str__(self):
        return '%s, %s'%(self.flag, self.lang.lang)