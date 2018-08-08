from django.urls import path

from .views import PicView, ImgView, LayoutView

apps_name = 'kuukann'

urlpatterns = [
    path('pic', PicView.as_view() ),
    path('layout', LayoutView.as_view() ),
    path('pic/img', ImgView.as_view() ),
]