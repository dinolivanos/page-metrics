from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .tasks import add
from .models import Page, Metric, Report
from django.forms import ModelForm
from django.urls import reverse


def index(request):
    return HttpResponse("Dino was here")


def reports(request):
    print('DINO reports')
    add.delay(3, 4)
    return HttpResponse("reports")


def compare(request):
    return HttpResponse("compare")


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


def page(request, page_id):
    pass


def pages_delete(request, pageid):
    if request.method == 'POST':
        page = Page.objects.get(pk=pageid)
        page.delete()
        return HttpResponseRedirect(reverse('pages'))

def lighthouse_report(request):
    return render(request, 'metricsapp/lighthouse-report.html')