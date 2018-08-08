# Import
# here that import Python module

from django.contrib import admin

# Import 
# here that import your module
from .models import KuuKann, Pic, Img, Layout, CompMsg
from ..vcr_conf import pre_page_num, none_show, admin_title, admin_header

# admin conf
admin.site.site_title = admin_title
admin.site.site_header = admin_header
# Register your models here.

# Register your models here.

class KuuKannAdmin(admin.ModelAdmin):
    list_display = ('name', 'kouza', 'status', 'create_date')
    list_display_links = ('name', )

    list_per_page = pre_page_num
    list_filter = ('status',)
    search_fields = ('name', )

    date_hierarchy = 'create_date'
    empty_value_display = none_show

class LayoutAdmin(admin.ModelAdmin):
    list_display = ('order_by', 'layout_name', 'diy_w', 'diy_h', 'grid_name')
    list_display_links = ('order_by', 'layout_name', 'diy_w', 'diy_h', 'grid_name')

    list_per_page = pre_page_num

class PicAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'update_date')
    list_display_links = ('name', )

    list_per_page = pre_page_num
    list_filter = ('name', )
    search_fields = ('name', )

    date_hierarchy = 'update_date'
    empty_value_display = none_show
    
class ImgAdmin(admin.ModelAdmin):
    list_display = ('pic', 'status', 'has_full', 'tiny_img', 'create_date')
    list_display_links = ('pic', 'status', 'has_full')

    list_per_page = pre_page_num
    list_filter = ('pic', )
    search_fields = ('pic', )

    date_hierarchy = 'create_date'
    empty_value_display = none_show

class CompMsgAdmin(admin.ModelAdmin):
    list_display = ('name', 'w', 'h', 'px', 'fmt', 'ratio', 'comp_time', 'content')
    list_display_links = ('name', 'w', 'h', 'px', 'fmt')

    list_per_page = pre_page_num
    list_filter = ('fmt', )
    search_fields = ('name', )

    empty_value_display = none_show

admin.site.register(KuuKann, KuuKannAdmin)
admin.site.register(Layout, LayoutAdmin)
admin.site.register(Pic, PicAdmin)
admin.site.register(Img, ImgAdmin)
admin.site.register(CompMsg, CompMsgAdmin)