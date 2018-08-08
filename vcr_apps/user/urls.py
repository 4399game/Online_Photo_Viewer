# Import
# here that python module
from django.urls import path, re_path

# Import
# here that you module
from ..user.views import StationView, StyleView, SafeView, SettingView

apps_name = 'user'

urlpatterns = [
    path('ゴミはこ/<str:station_flag>', StationView.as_view() ),
    path('ジェント', StyleView.as_view() ),
    path('safe', SafeView.as_view() ),
    path('setting', SettingView.as_view() ),
]