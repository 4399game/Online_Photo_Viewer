# Import
# here that import Python module

from django.contrib import admin

# Import 
# here that import your module
from .models import Lang, Text
from ..vcr_conf import pre_page_num, none_show, admin_title, admin_header

# admin conf
admin.site.site_title = admin_title
admin.site.site_header = admin_header
# Register your models here.

class LangAdmin(admin.ModelAdmin):
    list_display = ('lang', )
    list_display_links = ('lang', )

class TextAdmin(admin.ModelAdmin):
    list_display = ('lang', 'page', 'flag','content')
    list_display_links = ('lang', )
    list_editable = ('page', 'flag')

    list_per_page = pre_page_num
    list_filter = ('lang', 'page', 'flag')
    search_fields = ('content', )

admin.site.register(Lang, LangAdmin)
admin.site.register(Text, TextAdmin)