from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .tasks import generate_lighthouse_report
from .models import Page, Metric, Report
from django.forms import ModelForm
from django.urls import reverse
from django.http import Http404
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.safestring import mark_safe
from .metrics import lighthouse_scores, ACCESSIBILITY, PERFORMANCE, PWA, BEST_PRACTICES, SEO
import os



def index(request):
    return HttpResponse("Nothing to see")


def report(request, reportid):
    report = Report.objects.get(pk=reportid)
    if report.metric.name == 'lighthouse':
        report_path = static(report.report.replace('/static/metricsapp', '')) + '.report.html'
        print('report path {}'.format(report_path))
        context = {'report_path': report_path}
        return render(request, 'metricsapp/lighthouse-report.html', context)

    else:
        raise Http404("Poll does not exist")


def reports_generate(request):
    pages = Page.objects.all()
    for page in pages:
        generate_lighthouse_report.delay(page.url)

    return HttpResponseRedirect(reverse('pages'))


category_metric_map = {'performance': PERFORMANCE,
                       'pwa': PWA,
                       'accessibility': ACCESSIBILITY,
                       'seo': SEO}

def compare(request, category):
    print('cwd {}'.format(os.getcwd()))
    pages = Page.objects.all()
    data = []
    for page in pages:
        reports = Report.objects.filter(page=page.id, metric__name='lighthouse')
        report = reports.first()
        print('report {} {}'.format(report.report, report.page.url))
        report_path = 'metricsapp' + static(report.report.replace('/static/metricsapp', '')) + '.report.json'
        scores = lighthouse_scores(report_path)
        data.append({"name": report.page.url, "value": int(scores[category_metric_map[category]])})

    context = {'category': 'category', 'data': mark_safe(data)}
    return render(request, 'metricsapp/compare.html', context)


class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ['url', 'description']


def pages(request):
    if request.method == 'POST':
        page_form = PageForm(request.POST)
        if page_form.is_valid():
            page_form.save()
            return HttpResponseRedirect(reverse('pages'))
    else:
        page_form = PageForm()

    pages_list = Page.objects.all()
    context = {'pages': pages_list, 'form': page_form}
    return render(request, 'metricsapp/pages.html', context)


def page(request, pageid):
    page = Page.objects.get(pk=pageid)
    reports_list = Report.objects.filter(page=page.id)
    print('page reports {}'.format(reports_list.count()))
    context = {'page': page, 'reports': reports_list}
    return render(request, 'metricsapp/page.html', context)


def pages_delete(request, pageid):
    if request.method == 'POST':
        page = Page.objects.get(pk=pageid)
        page.delete()
        return HttpResponseRedirect(reverse('pages'))


def lighthouse_report(request):
    return render(request, 'metricsapp/lighthouse-report.html')


def test_site(request, param):
    context = {'param': param}
    return render(request, 'metricsapp/test_site.html', context)
