# Import
# here that import Python module
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.db.models import Q

# Import 
# here that import your module
from ..vcr_conf import (
                        key_kouza,
                        kouza_url, station_url,
                        station_pic_flag, station_img_flag
)
from .models import Station
from vcr_apps.kuukann.models import Pic, Img
from vcr_extra.vcr_util.station import false_date

# Create your views here.
"""
    搜索
"""
class SearchView(View):
    def get(self, request, search_txt, station_flag):
        search_flag = ''
        if search_txt and (search_txt is not 'tiny'):
            station_list = []
            kouza = request.session.get(key_kouza, None)
            station_queryset = Station.manager_one.filter(Q(kouza_id = kouza.id) & Q(status = True) & Q(station_flag = station_flag))

            if station_flag == station_pic_flag:
                search_queryset = Pic.manager_one.filter(Q(name__contains = search_txt) & Q(kouza_id = kouza.id))
                station_list = [station for station in station_queryset if station.pic.id in [pic.id for pic in search_queryset]]
                search_flag = 'pic'
            elif station_flag == station_img_flag:
                search_queryset = Img.manager_one.filter(Q(tiny_img__contains = search_txt) & Q(kouza_id = kouza.id))
                station_list = [station for station in station_queryset if station.img.id in [img.id for img in search_queryset]]
                search_flag = 'img'
            if station_list:
                station_flag = 'search'
                return render(request, 'user/station.html', {
                    'station_flag': station_flag,
                    'page_flag': station_flag,
                    'search_text': search_txt,
                    'search_flag': search_flag,
                    'station_list': station_list
                })
            else:
                url = kouza_url + station_url + station_flag
                return HttpResponseRedirect(url)
        else:
            url = request.get_full_path()
            return HttpResponseRedirect(url)

"""
    回收站
"""
class StationView(View):
    def get(self, request):
        kouza = request.session.get(key_kouza, None)
        station_flag = request.GET.get('station_flag', None)
        start_num = int(request.GET.get('start_num', None) )
        end_num = int(request.GET.get('end_num', None) )
        if station_flag == station_img_flag:
            false_date_list = []
            data_list = []
            station_queryset = Station.manager_one.filter(Q(kouza_id = kouza.id) & Q(status = True) & Q(station_flag = station_img_flag))[start_num: end_num: ]
            for sq in station_queryset:
                fd, f = false_date(sq.unshow_date, False)
                date = {
                    'date_flag': f,
                    'date_value': fd
                }
                false_date_list.append(date)
                data = {
                    'id' : sq.id,
                    'tiny_img': str(sq.img.tiny_img),
                }
                data_list.append(data)
            if false_date_list:
                return JsonResponse({
                    'has_data': True,
                    'data_list': data_list,
                    'date_list': false_date_list,
                    }, 
                    safe = False)
            else:
                return JsonResponse({'has_data': False})
        return HttpResponse(False)