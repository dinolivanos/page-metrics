from celery import shared_task, states
import time
from django_celery_results.models import TaskResult
from .metrics import lighthouse_generate_report as lighthouse_metrics
from .models import Page, Report, Metric, PENDING, SUCCESS, FAILED
import datetime
import pytz


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
    print('lighthouse url')
    metric = Metric.objects.get(name='lighthouse')
    page = Page.objects.get(url=url)
    report = Report.objects.create(page=page,
                                   metric=metric,
                                   status_date=datetime.datetime.now(pytz.utc),
                                   status=PENDING,
                                   report='')

    report.save()
    print('lighthouse report start')
    report_id = report.id
    report_path = './metricsapp/static/metricsapp/{}'.format(report_id)
    result = lighthouse_metrics(url, report_path + '.json')
    print('lighthouse report end {}'.format(result.returncode))
    report.status_date = datetime.datetime.now(pytz.utc)
    if result.returncode == 0:
        report.status = SUCCESS
        report.report = report_path
    else:
        report_id.status = FAILED

    report.save()
