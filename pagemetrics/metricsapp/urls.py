from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reports', views.reports, name='reports'),
    path('compare', views.compare, name='compare'),
    path('pages', views.pages, name='pages'),
    path('pages/<int:pageid>', views.page, name='page'),
    path('pages/<int:pageid>/delete', views.pages_delete, name='pages-delete'),
]
