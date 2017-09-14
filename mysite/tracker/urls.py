from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^linealComparativo/(?P<term_id>[1-3])/(?P<group_id>[1-7])/$', views.linealComparativo, name='linealComparativo'),
    url(r'^pieChartGrupal/(?P<term_id>[1-3])/(?P<group_id>[1-7])/$', views.pieChartGrupal, name='pieChartGrupal'),
    url(r'^circularAplicaciones/(?P<term_id>[1-3])/(?P<group_id>[1-7])/$', views.circularAplicaciones, name='circularAplicaciones'),
    url(r'^graficaProductividad/(?P<term_id>[1-3])/(?P<group_id>[1-7])/(?P<user_id>[0-9]+)/$', views.graficaProductividad, name='graficaProductividad'),
]
