# Import
# here that import Python module

from django.contrib import admin

# Import 
# here that import your module
from .models import KouZa, KouZaCtrl, Style, Setting, Safe, SafeAsk
from ..vcr_conf import pre_page_num, none_show, admin_title, admin_header

# admin conf
admin.site.site_title = admin_title
admin.site.site_header = admin_header
# Register your models here.

class KouZaAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'status')
    list_display_links = ('name', 'phone', 'email', 'status')

    list_per_page = pre_page_num
    search_fields = ('name', 'phone', 'email')

    # 字段为空显示的内容
    empty_value_display = none_show

class KouZaCtrlAdmin(admin.ModelAdmin):
    list_display = ('auth_num', 'layout', 'lang', 'def_kuukann', 'update_date')
    list_display_links = ('auth_num', 'layout', 'lang')

    list_per_page = pre_page_num
    list_filter = ('lang', 'auth_num')
    search_fields = ('layout','lang')

    empty_value_display = none_show

class StyleAdmin(admin.ModelAdmin):
    list_display = ('main_color', 'diy_color', 'name', 'bg_img')
    list_display_links = ('main_color', 'diy_color')
    
    list_per_page = pre_page_num
    list_filter = ('main_color', )
    search_fields = ('main_color', )

    empty_value_display = none_show

class SettingAdmin(admin.ModelAdmin):
    list_display = ('is_shen', 'is_doh', 'comp_ro', 'is_zhe', 'def_layout')
    list_display_links = ('is_shen', 'is_doh', 'comp_ro')
    
    list_per_page = pre_page_num
    list_filter = ('is_shen', )
    search_fields = ('is_doh', )

    empty_value_display = none_show

class SafeAskAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'status', 'safe')
    list_display_links = ('question', 'answer', 'status')
    
    list_per_page = pre_page_num
    list_filter = ('question', )
    search_fields = ('question', )

    empty_value_display = none_show

class SafeAdmin(admin.ModelAdmin):
    list_display = ('kuuk_pwd', 'ctrl_pwd', 'is_tell', 'is_mail', 'which_jm')
    list_display_links = ('kuuk_pwd', 'ctrl_pwd', 'is_tell', 'is_mail')
    
    list_per_page = pre_page_num
    list_filter = ('is_tell', 'is_mail', 'which_jm')
    search_fields = ('is_tell', 'is_mail')

    empty_value_display = none_show

admin.site.register(KouZa, KouZaAdmin)
admin.site.register(KouZaCtrl, KouZaCtrlAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(SafeAsk, SafeAskAdmin)
admin.site.register(Safe, SafeAdmin)