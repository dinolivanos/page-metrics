from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reports', views.reports, name='reports'),
    path('compare', views.compare, name='compare'),
    path('pages', views.pages, name='pages'),
]
