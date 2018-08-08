# Import
# here that import Python module
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.db.models import Q

# Import 
# here that import your module
from ..option.models import Station
from .models import Style, Safe
from ..vcr_conf import (
                        key_kouza,
                        station_pic_flag, station_img_flag
)

# Create your views here.

# Station
class StationView(View):
    def get(self, request, station_flag):
        kouza = request.session.get(key_kouza, None)
        if station_flag == station_pic_flag:
            station_queryset = Station.manager_one.filter(Q(kouza_id = kouza.id) & Q(status = True) & Q(station_flag = station_pic_flag))
            return render(request, 'user/station.html', {
                'station_list': station_queryset,
                'station_flag': station_flag,
                'page_flag': station_flag,
            })
        if station_flag == station_img_flag:
            return render(request, 'user/station.html', {
                'station_flag': station_flag,
                'page_flag': station_flag,
            })

    def put(self, request, station_flag):
        station_id = request.PUT.get('station_id', None)
        if station_flag == station_pic_flag:
            # 更改 相册
            station_pic = Station.manager_one.get(id = station_id)
            pic = station_pic.pic
            station_pic.status = False
            pic.status = True
            pic.save()
            station_pic.save()
        return HttpResponse(station_flag)


# Style
class StyleView(View):
    def get(self, request):
        kouza = request.session.get(key_kouza, None)
        style = Style.manager_one.get(kouza = kouza)
        return render(request, 'user/style.html', {
            'style': style
        })

# Safe 
class SafeView(View):
    def get(self, request):
        kouza = request.session.get(key_kouza, None)
        safe = Safe.manager_one.get(kouza = kouza)
        return render(request, 'user/safe.html', {
            'safe': safe
        })

# Setting      
class SettingView(View):
    def get(self, request):
        return render(request, 'user/setting.html')