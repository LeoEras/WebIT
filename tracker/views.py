from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Datos

filtros = ['stackoverflow', 'Stackoverflow', 'Komodo', 'komodo',
          'Notepad', 'notepad', 'cmd', 'localhost', 'python',
          'Python', 'Mongo', 'mongo', 'Sublime', 'sublime',
          'dllhost', 'wampmanager', 'Wampanager', 'NetBeans',
          'netbeans', 'github', 'GitHub', 'mintty', 'Mintty',
          'node', 'Node', 'server', 'Server']

def index(request):
    activity_list = Datos.objects.all()
    activity_list = filterByDateAndUser(activity_list, "2016-07-20", "2016-09-08", 22)
    for item in activity_list:
        setImportance(item, filtros)
    context = {'activity_list': activity_list}
    return render(request, 'tracker/index.html', context)
    
def base():
    pass

def setImportance(item, filters):
    for filtro in filters:
        if filtro in item.actividad or filtro in item.responsable:
            item.importancia = 1

def findItems(objects_list, name, item_type, date_start, date_end):
    result = []
    for item in objects:
        d_start = strToDate(date_start)
        item_date_start = strToDate(item[1])
        d_end = strToDate(date_end)
        item_date_end = strToDate(item[3])
        if d_start <= item_date_start and item_date_end <= d_end:
            if name == "":
                if item_type == "All":
                    if correctAll(item):
                        continue
                    else:
                        result.append(item)
                elif item_type in item[7]:
                    result.append(item)
            elif name in item[6]:
                result.append(item)
    return result

def filterByDate(objects, date_start, date_end):
    result = []
    d_start = datetime.strptime(date_start, "%Y-%m-%d").date()
    d_end = datetime.strptime(date_end, "%Y-%m-%d").date()
    for item in objects:
        if d_start <= item.dia_inicio and item.dia_final <= d_end:
            result.append(item)
    return result

def filterByDateAndUser(objects, date_start, date_end, user):
    result = []
    d_start = datetime.strptime(date_start, "%Y-%m-%d").date()
    d_end = datetime.strptime(date_end, "%Y-%m-%d").date()
    for item in objects:
        if item.usuario == user and d_start <= item.dia_inicio and item.dia_final <= d_end:
            result.append(item)
    return result



