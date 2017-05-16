from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^linealComparativo/(?P<grupo_id>[1-6])/$', views.linealComparativo, name='linealComparativo'),
    url(r'^pieChartGrupal/(?P<grupo_id>[1-6])/$', views.pieChartGrupal, name='pieChartGrupal'),
]
