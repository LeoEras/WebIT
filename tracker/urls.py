from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^linealComparativo/(?P<term_id>[1-2])/(?P<group_id>[1-6])/$', views.linealComparativo, name='linealComparativo'),
    url(r'^pieChartGrupal/(?P<term_id>[1-2])/(?P<group_id>[1-6])/$', views.pieChartGrupal, name='pieChartGrupal'),
    url(r'^circularAplicaciones/(?P<term_id>[1-2])/(?P<group_id>[1-6])/$', views.circularAplicaciones, name='circularAplicaciones'),
]
