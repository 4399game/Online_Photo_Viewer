# Import
# here that import Python module
import time
from django.shortcuts import render
from django.views import View
from django.db.models import Q
from django.http import HttpResponse

# Import 
# here that import your module
from PIL import Image
import greenlet
import cv2
from ...user.models import KouZa, KouZaCtrl
from vcr_apps.kuukann.models import Img
from ...vcr_conf import (
                        key_kouza, key_kouza_ctrl,
                        i_middle
)
from vcr_extra.vcr_util.img_compress import get_comp_ratio
from VcrT.settings import MEDIA_ROOT

# url请求时压缩图片
def img_compress(request, path):
    img = Image.open(path)
    x, y = img.size
    ratio = get_comp_ratio(x, y)
    new_size = ( int( x*ratio), int( y*ratio) )
    img = img.resize(new_size, Image.ANTIALIAS)
    response = HttpResponse(content_type = "image/png")
    img.save(response, "JPEG") # 将PIL的image对象写入response中，通过response返回

    return response

# Create your views here.
class TestCrooperView(View):
    def get(self, request):
        return render(request, 'test/image_crooper.html')

class TestViewerView(View):
    def get(self, request):
        img_list = Img.manager_two.all()
        return render(request, 'test/image_viewer.html',{
            'img_list': img_list
        })