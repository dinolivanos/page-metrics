from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reports/generate', views.reports_generate, name='reports-generate'),
    path('reports/<int:reportid>', views.report, name='report'),
    path('compare/<str:category>', views.compare, name='compare'),
    path('pages', views.pages, name='pages'),
    path('pages/<int:pageid>', views.page, name='page'),
    path('pages/<int:pageid>/delete', views.pages_delete, name='pages-delete'),
    path('lighthouse-report', views.lighthouse_report, name='lighthouse-report'),
    path('test_site/<int:param>', views.test_site, name='test-site'),
]
