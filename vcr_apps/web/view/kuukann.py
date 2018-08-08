# Import
# here that import Python module

import os
from django.shortcuts import render
from django.views import View
from django.db.models import Q
from django.http import JsonResponse

# Import 
# here that import your module
from ...kuukann.models import KuuKann, Pic, Img
from ...vcr_conf import (key_kouza,
                         kouza_path,
                         kuukann_url,
)
from vcr_extra.vcr_util.img import simple_image

# Create your views here.
class KuKannView(View):
    def get(self, request, name):
        kouza = request.session.get(key_kouza, None)
        kuukann = KuuKann.manager_two.get(Q(kouza = kouza) & Q(name = name))

        pic_queryset = Pic.manager_two.filter(kuukann_id = kuukann.id)
        return render(request, 'kuukann/pic.html' ,{
            'kuukann': kuukann,
            'page_flag': 'pic',
            'pic_list': pic_queryset
        })

class PicView(View):
    def get(self, request, kuukann_name, pic_name):
        # 跳转
        kouza = request.session.get(key_kouza, None)
        kuukann = KuuKann.manager_two.get(Q(kouza = kouza) & Q(name = kuukann_name))
        pic = Pic.manager_two.get(Q(kuukann = kuukann) & Q(name = pic_name))
        layout = pic.layout

        page_name = 'kuukann/img_'+ layout.layout_name +'.html'
        img_queryset = Img.manager_two.filter(pic_id = pic.id)
        return render(request, page_name, {
            'pic': pic,
            'layout': layout,
            'img_list': img_queryset,
            'previous_url': kuukann_url + kuukann_name
        })
        
    def post(self, request, kuukann_name, pic_name):
        # 修改 封面
        data = {}
        pic_id = request.POST.get('pic_id', None)
        pic = Pic.manager_one.get(id = pic_id)

        pic_name = request.POST.get('pic_name', None)
        pic_image = request.FILES.get('pic_image', None)
        pic.name = pic_name
        save_path = os.path.join(kouza_path, str(pic.kouza.id), str(pic.kuukann.id), 'cover')
        pic.image = simple_image(pic_image, save_path, 'comp')
        pic.save()
        data['id'] = pic_id
        data['name'] = pic.name
        data['image'] = str(pic.image)
        return JsonResponse(data, safe = False)

class ImgView(View):
    def get(self, request, pic_id):
        # 查询
        pic = Pic.manager_two.get(id = pic_id)
        layout = pic.layout

        page_name = 'kuukann/pic_'+ layout.layout_name +'.html'
        img_queryset = Img.manager_two.filter(pic_id = pic_id)
        return render(request, page_name, {
            'pic': pic,
            'layout': layout,
            'img_list': img_queryset,
        })


