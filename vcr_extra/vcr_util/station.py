import datetime
from django.utils import timezone

"""
def false_date(value, is_html):
    if is_html:
        d1 = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        now = datetime.datetime.now()
        dat = d1 - now
        value = dat.days + 1
        hour = dat.seconds/3600
        print('小时', hour, value)
        if value < 1:
            hour = dat.seconds/3600
            if hour < 1:
                return value
        if (value < 10) and (value >= 1):
            return '0' + str(value)
        return value
    else:
        now = timezone.now()
        dat = value - now
        value = dat.days + 1
        hour = dat.seconds/3600
        print('小时', hour, value)
        if value < 1:
            if hour < 1:
                return value
        if (value < 10) and (value >= 1):
            return '0' + str(value)
        return value

"""
def false_date(value, is_html):
    if is_html:
        d1 = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        now = datetime.datetime.now()
        dat = d1 - now
        value = dat.days + 1
        if value > 2:
            value = str(value) + ' days'
        elif value <2:
            second = dat.seconds
            hour = float('%.1f'%(second/3600))
            if hour < 1:
                minute = second/60
                value = str(minute) + ' minus'
            else:
                value = str(int(hour)) + ' hours'
        return value
    else:
        now = timezone.now()
        dat = value - now
        value = dat.days + 1
        f = 'day'
        if value > 2:
            value = value
        elif value <2:
            second = dat.seconds
            hour = float('%.1f'%(second/3600))
            if hour < 1:
                minute = second/60
                value = minute
                f = 'minute'
            else:
                value = int(hour)
                f = 'hour'
        return value, f