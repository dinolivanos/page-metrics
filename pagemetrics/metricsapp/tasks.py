from celery import shared_task, states
import time
from django_celery_results.models import TaskResult
from .metrics import lighthouse_generate_report
from .models import Page, Report, Metric

@shared_task(bind=True)
def add(self, x, y):
    print('DINO add')
    task_result = task_result = TaskResult(task_id=self.request.id)
    task_result.save()
    print('DINO add sleep')
    time.sleep(5)
    print('DINO add wake')
    task_result.status = states.SUCCESS
    task_result.save()
    print('DINO add return')
    return x + y


@shared_task(bind=True)
def generate_lighthouse_report(self, url):
    print(url)

    # create pending report in db
    # get report
    # update report status and file locations
