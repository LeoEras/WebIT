from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^linealComparativo/(?P<grupo_id>[0-9])/$', views.linealComparativo, name='linealComparativo'),
]

#r'^(?P<question_id>[0-9]+