# Import
# here that import Python module

from django.shortcuts import render
from django.views import View
from django.db.models import Q

# Import 
# here that import your module
from ...user.models import KouZa
from vcr_apps.kuukann.models import KuuKann
from ...vcr_conf import key_kouza

# Create your views here.
class IndexView(View):
    def get(self, request):
        session_vcrting = request.session.get(key_kouza, None)
        # if not exist vcrting
        if session_vcrting is None:
            # give the VcrT to the kouza
            kouza = KouZa.manager_one.get(Q(name = 'VcrT') & Q(status = None) )
            kuukann = KuuKann.manager_one.get(name = kouza.kouza_ctrl.def_kuukann)
            request.session[key_kouza ] = kouza
            request.session.set_expiry(0)
            """
            task_del_station_def.delay(
                kouza_id = kouza.id,
                status = False,
                keep_day = kouza.kouza_ctrl.keep_day
            )"""
        print('Here is index View get method !')
        return render(request, 'index.html', {
            'page_flag': 'index'
        })