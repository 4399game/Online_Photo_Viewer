# Import
# here that python module
from django.urls import path, re_path

# Import
# here that you module
from .views import StationView, SearchView

apps_name = 'option'

urlpatterns = [
    path('station', StationView.as_view() ),

    path('ルマスター/<str:search_txt>/<str:station_flag>', SearchView.as_view() ),
]