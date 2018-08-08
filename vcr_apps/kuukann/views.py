# Import
# here that import Python module
import os
import datetime
from django.views import View
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.db.models import Q
from django.utils import timezone

# Import 
# here that import your module
from .models import KuuKann, Pic, Img, Layout
from ..option.models import Station
from dateutil.relativedelta import relativedelta

from ..vcr_conf import (key_kouza,
                        kuukann_url,
                        i_middle, kouza_path,
                        station_pic_flag, station_img_flag
)
from ..web.vcr_task.img_task import task_dsi
from ..option.vcr_task.add_station import task_add_station
from vcr_extra.vcr_util.img_compress import get_img_msg
from vcr_extra.vcr_util.img import simple_image
# Some gloable


# Create your views here.

# Img
class ImgView(View):
    def get(self, request):
        # 查询
        select_flag = request.GET.get('select_flag', None)

        if select_flag == 'all':
            start_num = int(request.GET.get('start_num', None))
            end_num = int(request.GET.get('end_num', None))
            pic_id = request.GET.get('pic_id', None)
            pic = Pic.manager_two.get(id = pic_id)
            layout = Layout.manager_one.get(pic = pic)
            img_queryset = Img.manager_two.filter(pic = pic).order_by(layout.order_by)[start_num: end_num: ]
            data = {
                'img_list' : [{
                    'id' : img.id,
                    'w'  : img.width,
                    'h'  : img.height,
                    'has_full' : img.has_full,
                    'tiny_img' : str(img.tiny_img),
                    'less_img' : str(img.less_img),
                    'full_img' : str(img.full_img),
                    'create_date' : img.create_date
                } for img in img_queryset]
            }
        return JsonResponse(data, safe = False)

    def post(self, request):
        # 新增
        kouza = request.session.get(key_kouza, None)
        pic_id = request.POST.get('pic_id', None)
        img_image = request.FILES.get('img_image', None)

        pic = Pic.manager_two.get(id = pic_id)
        path = os.path.join(kouza_path, str(kouza.id), str(pic.kuukann.id), str(pic.id))
        
        w, h, fmt = get_img_msg(img_image)
        # 保存图片
        img = Img()
        img.create_date = timezone.now()
        img.pic = pic
        img.kouza = kouza
        if(w > i_middle) or (h > i_middle):
            # 储存 Img 对象
            img.has_full = True
            img.full_img = img_image
            img.less_img = simple_image(img_image, os.path.join(path, 'less'), 'comp')
            img.save()  

            # Celery 异步压缩
            task_dsi.delay(img.id , path, fmt)
        else:
            img.tiny_img = img_image
            img.width = w
            img.height = h
            img.has_full = False
            img.less_img = simple_image(img_image, os.path.join(path, 'less'), 'comp')

            # 储存 Img 对象
            img.save()
        return HttpResponse(img.id)
    
    def put(self, request):
        return HttpResponse(True)

    def delete(self, request):
        pic_id = request.DELETE.get('pic_id', None)
        del_img_l = request.DELETE.get('del_img_id', None)

        id_list = [i for i in del_img_l.split('_') if (i != '') and (i != None)]
        for id in id_list:
            img = Img.manager_two.get(id = id)
            img.status = False
            
            pic = Pic.manager_two.get(id = pic_id)
            kouza = pic.kouza
            kouza_ctrl = kouza.kouza_ctrl
            date_now = timezone.now()
            date_futrue = datetime.date.today() - relativedelta(hours= -kouza_ctrl.keep_day)

            station = Station()
            try:
                station = Station.manager_one.get(Q(img_id = img.id) & Q(station_flag = station_img_flag))
                station.status = True
                station.false_date = date_now
                station.unshow_date = date_futrue
            except:
                station.pic = pic
                station.kouza = kouza
                station.img = img
                station.status = True
                station.station_flag = station_img_flag
                station.false_date = date_now
                station.unshow_date = date_futrue

            station.save()
            img.save()
        return HttpResponse(del_img_l)

# Layout
class LayoutView(View):
    def post(self,request):
        try:
            pic_id = request.POST.get('pic_id', None)
            pic = Pic.manager_two.get(id = pic_id)
            order_by_name = request.POST.get('order_by', None)
            layout_name = request.POST.get('layout_name', None)
            grid_name = request.POST.get('grid_name', None)
            diy_w = float(request.POST.get('diy_w', None))
            diy_h = float(request.POST.get('diy_h', None))

            layout = pic.layout
            layout.order_by = order_by_name
            layout.layout_name = layout_name
            if (diy_w >= 1000) or (diy_h >= 1000):
                diy_w /= 100
                diy_h /= 100
            layout.diy_w = diy_w
            layout.diy_h = diy_h
            layout.grid_name = grid_name
            layout.save()
            url = kuukann_url + pic.kuukann.name + '/' + pic.name
        except:
            kouza = request.session.get(key_kouza, None)
            url = kuukann_url+ str(kouza.def_kuukann)
        return HttpResponseRedirect(url)  

    def put(self, request):
        edit_flag = request.PUT.get('edit_flag', None)
        pic_id = request.PUT.get('pic_id', None)
        pic = Pic.manager_two.get(id = pic_id)

        layout = pic.layout
        if edit_flag == 'grid':
            grid_name = request.PUT.get('grid_name', None)
            layout.grid_name = grid_name

        layout.save() 
        return HttpResponse(True)      

# Pic
class PicView(View):
    def get(self, request):
        # 查询
        data = {}
        flag = request.GET.get('select_flag', None)

        if flag == 'one':
            pic_id = request.GET.get('pic_id', None)
            pic = Pic.manager_two.get(id = pic_id)
            data['id'] = pic_id
            data['name'] = pic.name
            data['image'] = str(pic.image)
            return JsonResponse(data)
        elif flag == 'last':
            kouza = request.session.get(key_kouza, None)
            pic = Pic.manager_two.get(kouza = kouza).last()
            data['create_date'] = pic.create_date
        elif flag == 'all':
            kuukann_id = request.GET.get('kuukann_id', None)
            pic_queryset = Pic.manager_two.filter(kuukann_id = kuukann_id)
            data = [{
                    'id': pic.id,
                    'name': pic.name,
                    'image': str(pic.image),
                    'create_date': pic.create_date
            } for pic in pic_queryset]
            return JsonResponse(data, safe = False)

    def post(self, request):
        # 增加
        kouza = request.session.get(key_kouza, None)
        kuukann_name = request.POST.get('kuukann_name', None)
        pic_name = request.POST.get('pic_name', None)
        pic_image = request.FILES.get('pic_image', None)
        kuukann = KuuKann.manager_two.get(Q(name = kuukann_name) & Q(kouza = kouza))

        layout = Layout()
        layout.save()
        
        pic = Pic()
        pic.name = pic_name
        pic.image = pic_image
        pic.kouza = kouza
        pic.kuukann = kuukann
        pic.layout = layout
        pic.create_date = timezone.now()
        pic.save()

        img = Img()
        img.tiny_img = pic_image
        img.less_img = pic_image
        img.full_img = pic_image
        img.pic = pic
        img.status = None
        img.save()

        return HttpResponse(pic.id)

    def put(self, request):
        # 修改 名称
        data = {}
        pic_id = request.PUT.get('pic_id', None)
        pic = Pic.manager_one.get(id = pic_id)

        pic_name = request.PUT.get('pic_name', None)
        pic.name = pic_name
        pic.save()
        data['id'] = pic_id
        data['name'] = pic_name
        return JsonResponse(data)

    def delete(self, request):
        # 删除
        kouza = request.session.get(key_kouza, None)
        kuukann_id = request.DELETE.get('kuukann_id', None)
        pic_id_l = request.DELETE.get('pic_id', None)
        id_list = [int(i) for i in pic_id_l.split('_') if (i != '') and (i != None)]
        pic_queryset = Pic.manager_two.filter(Q(kouza = kouza) & Q(kuukann_id = kuukann_id))
        for pic in pic_queryset:
            if pic.id in id_list:
                pic.status = False
                pic.save()
                task_add_station.delay(station_pic_flag, {
                    'pic_id': pic.id,
                    'status': True,
                })

        return JsonResponse({'pic_id_l': id_list})