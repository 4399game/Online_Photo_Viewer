import time
import celery
from celery.utils.log import get_task_logger

log = get_task_logger(__name__)

# 测试 celery
@celery.task
def log_test(self):
    log.debug('in log_test(), test start ~')
    time.sleep(60)
    log.debug('test_task end ~')