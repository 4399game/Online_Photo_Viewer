from celery.task.schedules import crontab
from celery.decorators import periodic_task
from django.utils import timezone
# Your Task
@periodic_task(run_every = crontab(minute = '*', hour = '*', day_of_week = '*', day_of_month = '*', month_of_year = '*'))
def task_del_station_def(kouza_id, status, keep_day):
    print('---- start ----')
    print('now = ', timezone.now())
    print('---- end ----')