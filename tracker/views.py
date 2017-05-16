from django.shortcuts import render
from datetime import date, datetime, timedelta
import operator
from collections import Counter
from .models import Datos

def index(request):
    context = fetchDocInfofromUser(22)
    context = {'context': context}
    return render(request, 'tracker/grupo1.html', context)
    
def pieChartGrupal(request, grupo_id):
    users = groupSelector(grupo_id)
    list_1 = fetchAllInfofromUser(users[0])
    list_2 = fetchAllInfofromUser(users[1])
    list_3 = fetchAllInfofromUser(users[2])
    list_4 = fetchAllInfofromUser(users[3])
    dataset_1 = classifyUsefullness(list_1)
    dataset_2 = classifyUsefullness(list_2)
    dataset_3 = classifyUsefullness(list_3)
    dataset_4 = classifyUsefullness(list_4)
    uful_1, uless_1 = getTopActivitiesCircular(list_1)
    uful_2, uless_2 = getTopActivitiesCircular(list_2)
    uful_3, uless_3 = getTopActivitiesCircular(list_3)
    uful_4, uless_4 = getTopActivitiesCircular(list_4)
    context = {'dataset_1': dataset_1,
               'dataset_2': dataset_2,
               'dataset_3': dataset_3,
               'dataset_4': dataset_4,
               'uful_1': uful_1,
               'uless_1': uless_1,
               'uful_2': uful_2,
               'uless_2': uless_2,
               'uful_3': uful_3,
               'uless_3': uless_3,
               'uful_4': uful_4,
               'uless_4': uless_4,
               'grupo_id': grupo_id}
    return render(request, 'tracker/pieChartGrupal.html', context)

def linealComparativo(request, grupo_id):
    users = groupSelector(grupo_id)
    all_dates = []
    list_1 = fetchDocInfofromUser(users[0])
    sorted_dates_1, times_1 = buildDataset(list_1)
    list_2 = fetchDocInfofromUser(users[1])
    sorted_dates_2, times_2 = buildDataset(list_2)
    list_3 = fetchDocInfofromUser(users[2])
    sorted_dates_3, times_3 = buildDataset(list_3)
    list_4 = fetchDocInfofromUser(users[3])
    sorted_dates_4, times_4 = buildDataset(list_4)
    all_dates = sorted_dates_1 + list(set(sorted_dates_2) - set(sorted_dates_1))
    all_dates = all_dates + list(set(sorted_dates_3) - set(all_dates))
    all_dates = all_dates + list(set(sorted_dates_4) - set(all_dates))
    all_dates = sorted(all_dates)
    times_1 = depurateTimes(all_dates, sorted_dates_1, times_1)
    times_2 = depurateTimes(all_dates, sorted_dates_2, times_2)
    times_3 = depurateTimes(all_dates, sorted_dates_3, times_3)
    times_4 = depurateTimes(all_dates, sorted_dates_4, times_4)
    context = {'times_1': times_1,
               'times_2': times_2,
               'times_3': times_3,
               'times_4': times_4,
               'dates': all_dates,
               'group_id': grupo_id}
    return render(request, 'tracker/linealComparativo.html', context)
    
##def groupSelector(grupo_id):
##    if grupo_id in '1':
##        user_1 = 22
##        user_2 = 26
##        user_3 = 28
##        user_4 = 34
##    elif grupo_id in '2':
##        user_1 = 23
##        user_2 = 32
##        user_3 = 36
##        user_4 = 41
##    elif grupo_id in '3':
##        user_1 = 29
##        user_2 = 30
##        user_3 = 31
##        user_4 = 38
##    elif grupo_id in '4':
##        user_1 = 27
##        user_2 = 37
##        user_3 = 39
##        user_4 = 40
##    elif grupo_id in '5':
##        user_1 = 26
##        user_2 = 33
##        user_3 = 34
##        user_4 = 43
##    else:
##        user_1 = 22
##        user_2 = 28
##        user_3 = 35
##        user_4 = 25
##    return [user_1, user_2, user_3, user_4]

def groupSelector(grupo_id):
    if grupo_id in '1':
        user_1 = 1
        user_2 = 2
        user_3 = 18
        user_4 = 0
    elif grupo_id in '2':
        user_1 = 4
        user_2 = 10
        user_3 = 22
        user_4 = 0
    elif grupo_id in '3':
        user_1 = 8
        user_2 = 9
        user_3 = 0
        user_4 = 0
    elif grupo_id in '4':
        user_1 = 7
        user_2 = 13
        user_3 = 15
        user_4 = 0
    elif grupo_id in '5':
        user_1 = 5
        user_2 = 17
        user_3 = 0
        user_4 = 0
    elif grupo_id in '6':
        user_1 = 3
        user_2 = 6
        user_3 = 21
        user_4 = 0
    else:
        user_1 = 1
        user_2 = 2
        user_3 = 18
        user_4 = 0
    return [user_1, user_2, user_3, user_4]

def depurateTimes(dates_set, sorted_dates, sorted_times):
    new_times = [0 for item in range(0, len(dates_set))]
    for i in range(0, len(dates_set)):
        if dates_set[i] in sorted_dates:
            index = sorted_dates.index(dates_set[i])
            new_times[i] = sorted_times[index]
    return new_times

def classifyUsefullness(dataset):
    dictionary = {}
    dictionary["useful"] = 0
    dictionary["useless"] = 0
    for item in dataset:
        if item.importancia == 1:
            dictionary["useful"] += (datetime.combine(date.min, item.tiempo) - datetime.min).total_seconds()
        else:
            dictionary["useless"] += (datetime.combine(date.min, item.tiempo) - datetime.min).total_seconds()
    return dictionary

def fetchDocInfofromUser(user):
    user_activity = Datos.objects.filter(usuario=user)
    #user_activity = filterByDate(user_activity, "2016-07-21", "2016-09-08")
    user_activity = filterByDate(user_activity, "2017-01-01", "2017-03-05")
    user_activity = filterByClass(user_activity, "Documents")
    user_activity = filterByRelevance(user_activity, 1)
    return user_activity

def fetchAppInfofromUser(user):
    user_activity = Datos.objects.filter(usuario=user)
    user_activity = filterByDate(user_activity, "2017-01-01", "2017-03-05")
    user_activity = filterByClass(user_activity, "Applications")
    return user_activity

def fetchAllInfofromUser(user):
    user_activity = Datos.objects.filter(usuario=user)
    user_activity = filterByDate(user_activity, "2017-01-01", "2017-03-05")
    user_activity = filterByClass(user_activity, "Documents")
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

def getTopActivitiesCircular(activity_list):
    dictionary_uful = {}
    dictionary_uless = {}
    for item in activity_list:
        if '.js' in item.responsable or '.css' in item.responsable or '.ejs' in item.responsable or '.html' in item.responsable:
            continue
        if item.importancia == 1:
            if item.responsable not in dictionary_uful:
                dictionary_uful[item.responsable] = (datetime.combine(date.min, item.tiempo) - datetime.min).total_seconds()
            else:
                dictionary_uful[item.responsable] += (datetime.combine(date.min, item.tiempo) - datetime.min).total_seconds()
        else:
            if item.responsable not in dictionary_uless:
                dictionary_uless[item.responsable] = (datetime.combine(date.min, item.tiempo) - datetime.min).total_seconds()
            else:
                dictionary_uless[item.responsable] += (datetime.combine(date.min, item.tiempo) - datetime.min).total_seconds()
                
    return Counter(dictionary_uful).most_common(5), Counter(dictionary_uless).most_common(5)
    
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


