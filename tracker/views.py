from django.shortcuts import render
from .models import Datos

def index(request):
    activity_list = Datos.objects.order_by('id')
    context = {'activity_list': activity_list}
    return render(request, 'tracker/index.html', context)
    
def base():
    pass