import os
import datetime
from django import template
from django.utils import timezone

from vcr_extra.vcr_util.station import false_date

register = template.Library()

@register.filter(name='station_day')
def station_day(value):
    return false_date(value, True)

@register.filter(name='defnull')
def def_null(value, text):
    if value == '':
        return text
    elif value == None:
        return text
    return value