from django.test import TestCase

# Create your tests here.
import datetime
import pytz
from .models import *


class MetricTestCase(TestCase):

    def setUp(self):
        Metric.objects.create(name='metric', description='description')

    def test_metric(self):
        metric = Metric.objects.get(name='metric')
        self.assertEqual(metric.name, 'metric')
        self.assertEqual(metric.description, 'description')


class PageTestCase(TestCase):

    def setUp(self):
        Page.objects.create(url='http://www.test.com', description='description')

    def test_metric(self):
        page = Page.objects.get(url='http://www.test.com')
        self.assertEqual(page.url, 'http://www.test.com')
        self.assertEqual(page.description, 'description')


class ReportTestCase(TestCase):
    success_date = datetime.datetime(2018, 12, 2, tzinfo=pytz.utc)
    def setUp(self):
        metric = Metric.objects.create(name='metric', description='description')
        page = Page.objects.create(url='http://www.test.com', description='description')

        report1 = Report.objects.create(page=page,
                                        metric=metric,
                                        status_date=datetime.datetime(2018, 12, 1, 0, 0, tzinfo=pytz.utc),
                                        status=SUCCESS,
                                        report='file:///report/here')


        report2 = Report.objects.create(page=page,
                                        metric=metric,
                                        status_date=ReportTestCase.success_date,
                                        status=PENDING,
                                        report='file:///report2/here')

    def test_page_reports(self):
        page = Page.objects.get(url='http://www.test.com')

        reports = page.reports.all()
        self.assertEqual(reports.count(), 2)

    def test_reports_status(self):
        pending_reports = Report.objects.filter(status=PENDING)
        self.assertEqual(pending_reports.count(), 1)
        self.assertEqual(pending_reports[0].status, PENDING)
        self.assertEqual(pending_reports[0].status_date, ReportTestCase.success_date)

        success_reports = Report.objects.filter(status=SUCCESS)
        self.assertEqual(success_reports.count(), 1)
        self.assertEqual(success_reports[0].status, SUCCESS)
