from django.shortcuts import render
from django.http import HttpResponse
from .tasks import add
from .models import Page, Metric, Report


def index(request):
    return HttpResponse("Dino was here")


def reports(request):
    print('DINO reports')
    add.delay(3, 4)
    return HttpResponse("reports")


def compare(request):
    return HttpResponse("compare")


def pages(request):
    pages_list = Page.objects.all()
    context = {'pages': pages_list}
    return render(request, 'metricsapp/pages.html', context)
