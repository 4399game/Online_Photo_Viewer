# Import
# here that python module
from django.urls import path, re_path

# Import
# here that you module
from .view.vcr import IndexView
from .view.kuukann import KuKannView, PicView, ImgView
from .view.func import TestCrooperView, img_compress, TestViewerView

apps_name = 'web'

urlpatterns = [
    path('', IndexView.as_view() ),
    path('域/<str:name>', KuKannView.as_view() ),
    path('域/<str:kuukann_name>/<str:pic_name>', PicView.as_view() ),

    # path('test_crooper', TestCrooperView.as_view() ),
    # path('test_viewer', TestViewerView.as_view() ),

    re_path('^imgcomp/(?P<path>(.+))/$', img_compress),
]