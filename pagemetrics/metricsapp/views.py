from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .tasks import add

def index(request):
    return HttpResponse("Dino was here")

def reports(request):
    print('DINO reports')
    add.delay(3,4)
    return HttpResponse("reports")

def compare(request):
    return HttpResponse("compare")