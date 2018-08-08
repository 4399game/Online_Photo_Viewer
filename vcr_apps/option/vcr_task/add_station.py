import datetime
from celery import task
from django.utils import timezone
from django.db.models import Q
from vcr_apps.kuukann.models import Pic, Img
from vcr_apps.option.models import Station
from vcr_apps.vcr_conf import (
                        station_pic_flag
)

from dateutil.relativedelta import relativedelta
# Your Task
@task()
def task_add_station(station_flag, data):
    if station_flag == station_pic_flag:
        s_flag = False
        pic_id = data['pic_id']
        status = data['status']
        pic = Pic.manager_one.get(id = pic_id)
        kouza = pic.kouza
        kouza_ctrl = kouza.kouza_ctrl
        date_now = timezone.now()
        date_futrue = datetime.date.today() - relativedelta(hours= -kouza_ctrl.keep_day)
        try:
            pic_station = Station.manager_one.get(Q(pic_id = pic_id) & Q(station_flag = station_pic_flag))
            s_flag = True
        except:
            pass

        # 保存station
        if s_flag:
            pic_station.status = status
            pic_station.false_date = date_now
            pic_station.unshow_date = date_futrue
            pic_station.save()
        else:
            pic_station = Station()
            img = Img.manager_one.get(Q(id = 1) & Q(status = None))
            pic_station.img = img
            pic_station.pic = pic
            pic_station.kouza = pic.kouza
            pic_station.status = status
            pic_station.station_flag = station_flag
            pic_station.false_date = date_now
            pic_station.unshow_date = date_futrue
            pic_station.save()

        # 更改图片
        """
        if s_flag:
            station_img_queryset = Station.manager_one.filter(Q(pic_id = pic.id) & Q(station_flag = station_img_flag))
            for siq in station_img_queryset:
                siq.status = status
                siq.false_date = date_now
                siq.unshow_date = date_futrue
                siq.save()
        else:
            img_queryset = Img.manager_one.filter(Q(pic_id = pic_id) & Q(status = True))
            for img in img_queryset:
                station = Station()
                station.pic = pic
                station.kouza = kouza
                station.status = status
                station.img = img
                station.station_flag = station_img_flag
                station.false_date = date_now
                station.unshow_date = date_futrue
                station.save()
        """