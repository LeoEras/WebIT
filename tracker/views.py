from django.shortcuts import render
from datetime import date, datetime, timedelta
from .models import Datos

def index(request):
    all_dates = []
    list_22 = fetchInfofromUser(22)
    sorted_dates_22, times_22 = buildDataset(list_22)
    list_28 = fetchInfofromUser(28)
    sorted_dates_28, times_28 = buildDataset(list_28)
    list_34 = fetchInfofromUser(34)
    sorted_dates_34, times_34 = buildDataset(list_34)
    list_26 = fetchInfofromUser(26)
    sorted_dates_26, times_26 = buildDataset(list_26)
    all_dates = sorted_dates_22 + list(set(sorted_dates_28) - set(sorted_dates_22))
    all_dates = all_dates + list(set(sorted_dates_34) - set(all_dates))
    all_dates = all_dates + list(set(sorted_dates_26) - set(all_dates))
    all_dates = sorted(all_dates)
    times_22 = depurateTimes(all_dates, sorted_dates_22, times_22)
    times_28 = depurateTimes(all_dates, sorted_dates_28, times_28)
    times_34 = depurateTimes(all_dates, sorted_dates_34, times_34)
    times_26 = depurateTimes(all_dates, sorted_dates_26, times_26)
    context = {'times_22': times_22,
               'times_28': times_28,
               'times_34': times_34,
               'times_26': times_26,
               'dates': all_dates}
    return render(request, 'tracker/index.html', context)
    
def base():
    pass

def depurateTimes(dates_set, sorted_dates, sorted_times):
    new_times = [0 for item in range(0, len(dates_set))]
    for i in range(0, len(dates_set)):
        if dates_set[i] in sorted_dates:
            index = sorted_dates.index(dates_set[i])
            new_times[i] = sorted_times[index]
    return new_times

def fetchInfofromUser(user):
    user_activity = Datos.objects.filter(usuario=user)
    user_activity = filterByDate(user_activity, "2016-07-21", "2016-09-08")
    #user_activity = filterByClass(user_activity, "Applications")
    user_activity = filterByRelevance(user_activity, 1)
    return user_activity

def buildDataset(activity_list):
    dictionary = {}
    for item in activity_list:
        if item.dia_inicio not in dictionary:
            dictionary[item.dia_inicio] = (datetime.combine(date.min, item.tiempo) - datetime.min).total_seconds()
        else:
            dictionary[item.dia_inicio] += (datetime.combine(date.min, item.tiempo) - datetime.min).total_seconds()
    sorted_dates = sorted(dictionary)
    time_per_date = []
    for i in range(0, len(sorted_dates)):
        time_per_date.append(dictionary[sorted_dates[i]])
    return sorted_dates, time_per_date
    
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
        if item.dia_inicio >= d_start and item.dia_final <= d_end:
            result.append(item)
    return result

def filterByClass(objects, class_object):
    result = []
    for item in objects:
        if item.responsable == "Google Chrome":
            continue
        else:
            if item.clase == class_object:
                result.append(item)
    return result

def filterByRelevance(objects, relevance):
    result = []
    for item in objects:
        if item.importancia == relevance:
            result.append(item)
    return result


