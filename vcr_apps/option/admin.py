# Import
# here that import Python module

from django.contrib import admin

# Import 
# here that import your module
from .models import Station
from ..vcr_conf import pre_page_num, none_show, admin_title, admin_header

# admin conf
admin.site.site_title = admin_title
admin.site.site_header = admin_header

# Register your models here.
class StationAdmin(admin.ModelAdmin):
    list_display = ('kouza', 'pic', 'station_flag', 'img', 'status', 'false_date', 'unshow_date')
    list_display_links = ('kouza', 'pic', 'station_flag', )

    list_per_page = pre_page_num
    list_filter = ('status', 'station_flag')
    search_fields = ('kouza', 'pic', 'station_flag', 'img')
    date_hierarchy = 'false_date'
    
    empty_value_display = none_show

admin.site.register(Station, StationAdmin)