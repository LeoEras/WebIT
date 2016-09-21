from django.shortcuts import render
from .models import Datos

def index(request):
    latest_question_list = Datos.objects.order_by('-id')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'tracker/index.html', context)