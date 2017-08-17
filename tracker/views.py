from django.shortcuts import render
from datetime import date, datetime, timedelta
import operator
from collections import Counter
from .models import Log, Users, Dates, Class_Type, Term, Activity, Application
import re

def index(request):
    return render(request, 'tracker/index.html')
    
def pieChartGrupal(request, term_id, group_id):
    users = groupSelector(term_id, group_id)
    names = getNames(users, term_id)
    user_activity = Log.objects.filter(termID=term_id)
    if int(term_id) == 1:
        user_activity = filterByDate(user_activity, "2016-07-21", "2016-09-08")
    elif int(term_id) == 2:
        user_activity = filterByDate(user_activity, "2017-01-01", "2017-03-05")
    elif int(term_id) == 3:
        user_activity = filterByDate(user_activity, "2017-07-01", "2017-08-10")
    list_1 = fetchAllDocInfofromUser(user_activity, term_id, users[0])
    list_2 = fetchAllDocInfofromUser(user_activity, term_id, users[1])
    list_3 = fetchAllDocInfofromUser(user_activity, term_id, users[2])
    list_4 = fetchAllDocInfofromUser(user_activity, term_id, users[3])
    dataset_1 = classifyUsefullness(list_1)
    dataset_2 = classifyUsefullness(list_2)
    dataset_3 = classifyUsefullness(list_3)
    dataset_4 = classifyUsefullness(list_4)
    uful_1, uless_1 = getTopActivitiesCircular(list_1)
    uful_2, uless_2 = getTopActivitiesCircular(list_2)
    uful_3, uless_3 = getTopActivitiesCircular(list_3)
    uful_4, uless_4 = getTopActivitiesCircular(list_4)
    uful_1 = depurate(uful_1)
    uless_1 = depurate(uless_1)
    uful_2 = depurate(uful_2)
    uless_2 = depurate(uless_2)
    uful_3 = depurate(uful_3)
    uless_3 = depurate(uless_3)
    uful_4 = depurate(uful_4)
    uless_4 = depurate(uless_4)
    prev_id, next_id = getNextPrevious(term_id, group_id)
    max_groups = maxGroups(term_id)
    context = {'student1': names[0],
               'student2': names[1],
               'student3': names[2],
               'student4': names[3],
               'dataset_1': dataset_1,
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
               'group_id': group_id,
               'prev_id': prev_id,
               'next_id': next_id,
               'term_id': term_id,
               'max_groups': max_groups}
    return render(request, 'tracker/pieChartGrupal.html', context)

def linealComparativo(request, term_id, group_id):
    users = groupSelector(term_id, group_id)
    names = getNames(users, term_id)
    all_dates = []
    user_activity = Log.objects.filter(termID=term_id)
    if int(term_id) == 1:
        user_activity = filterByDate(user_activity, "2016-07-21", "2016-09-08")
    elif int(term_id) == 2:
        user_activity = filterByDate(user_activity, "2017-01-01", "2017-03-05")
    elif int(term_id) == 3:
        user_activity = filterByDate(user_activity, "2017-07-01", "2017-08-10")
    list_1 = fetchDocInfofromUser(user_activity, term_id, users[0])
    sorted_dates_1, times_1 = buildDataset(list_1)
    list_2 = fetchDocInfofromUser(user_activity, term_id, users[1])
    sorted_dates_2, times_2 = buildDataset(list_2)
    list_3 = fetchDocInfofromUser(user_activity, term_id, users[2])
    sorted_dates_3, times_3 = buildDataset(list_3)
    list_4 = fetchDocInfofromUser(user_activity, term_id, users[3])
    sorted_dates_4, times_4 = buildDataset(list_4)
    all_dates = sorted_dates_1 + list(set(sorted_dates_2) - set(sorted_dates_1))
    all_dates = all_dates + list(set(sorted_dates_3) - set(all_dates))
    all_dates = all_dates + list(set(sorted_dates_4) - set(all_dates))
    all_dates = sorted(all_dates)
    times_1 = depurateTimes(all_dates, sorted_dates_1, times_1)
    times_2 = depurateTimes(all_dates, sorted_dates_2, times_2)
    times_3 = depurateTimes(all_dates, sorted_dates_3, times_3)
    times_4 = depurateTimes(all_dates, sorted_dates_4, times_4)
    prev_id, next_id = getNextPrevious(term_id, group_id)
    max_groups = maxGroups(term_id)
    context = {'student1': names[0],
               'student2': names[1],
               'student3': names[2],
               'student4': names[3],
               'times_1': times_1,
               'times_2': times_2,
               'times_3': times_3,
               'times_4': times_4,
               'dates': all_dates,
               'group_id': group_id,
               'prev_id': prev_id,
               'next_id': next_id,
               'term_id': term_id,
               'max_groups': max_groups}
    return render(request, 'tracker/linealComparativo.html', context)

def circularAplicaciones(request, term_id, group_id):
    users = groupSelector(term_id, group_id)
    names = getNames(users, term_id)
    all_dates = []
    user_activity = Log.objects.filter(termID=term_id)
    if int(term_id) == 1:
        user_activity = filterByDate(user_activity, "2016-07-21", "2016-09-08")
    elif int(term_id) == 2:
        user_activity = filterByDate(user_activity, "2017-01-01", "2017-03-05")
    elif int(term_id) == 3:
        user_activity = filterByDate(user_activity, "2017-07-01", "2017-08-10")
    list_1 = fetchAppInfofromUser(user_activity, term_id, users[0])
    list_2 = fetchAppInfofromUser(user_activity, term_id, users[1])
    list_3 = fetchAppInfofromUser(user_activity, term_id, users[2])
    list_4 = fetchAppInfofromUser(user_activity, term_id, users[3])
    mat_1, list_1 = buildAppMatrix(list_1)
    mat_2, list_2 = buildAppMatrix(list_2)
    mat_3, list_3 = buildAppMatrix(list_3)
    mat_4, list_4 = buildAppMatrix(list_4)
    list_1 = getAppList(list_1)
    list_2 = getAppList(list_2)
    list_3 = getAppList(list_3)
    list_4 = getAppList(list_4)
    prev_id, next_id = getNextPrevious(term_id, group_id)
    max_groups = maxGroups(term_id)
    context = {'student1': names[0],
               'student2': names[1],
               'student3': names[2],
               'student4': names[3],
               'matrix_1': mat_1,
               'matrix_2': mat_2,
               'matrix_3': mat_3,
               'matrix_4': mat_4,
               'list_1': list_1,
               'list_2': list_2,
               'list_3': list_3,
               'list_4': list_4,
               'group_id': group_id,
               'prev_id': prev_id,
               'next_id': next_id,
               'term_id': term_id,
               'max_groups': max_groups}
    return render(request, 'tracker/circularAplicaciones.html', context)

##def circularActividades(request, term_id, group_id):
##    users = groupSelector(term_id, group_id)
##    names = getNames(users, term_id)
##    all_dates = []
##    user_activity = Log.objects.filter(termID=term_id)
##    if int(term_id) == 1:
##        user_activity = filterByDate(user_activity, "2016-07-21", "2016-09-08")
##    elif int(term_id) == 2:
##        user_activity = filterByDate(user_activity, "2017-01-01", "2017-03-05")
##    list_1 = fetchAppInfofromUser(user_activity, term_id, users[0])
##    list_2 = fetchAppInfofromUser(user_activity, term_id, users[1])
##    list_3 = fetchAppInfofromUser(user_activity, term_id, users[2])
##    list_4 = fetchAppInfofromUser(user_activity, term_id, users[3])
##    mat_1, list_1 = buildActMatrix(list_1)
##    mat_2, list_2 = buildActMatrix(list_2)
##    mat_3, list_3 = buildActMatrix(list_3)
##    mat_4, list_4 = buildActMatrix(list_4)
##    list_1 = getAppList(list_1)
##    list_2 = getAppList(list_2)
##    list_3 = getAppList(list_3)
##    list_4 = getAppList(list_4)
##    print(list_4)
##    prev_id, next_id = getNextPrevious(term_id, group_id)
##    context = {'student1': names[0],
##               'student2': names[1],
##               'student3': names[2],
##               'student4': names[3],
##               'matrix_1': mat_1,
##               'matrix_2': mat_2,
##               'matrix_3': mat_3,
##               'matrix_4': mat_4,
##               'list_1': list_1,
##               'list_2': list_2,
##               'list_3': list_3,
##               'list_4': list_4,
##               'group_id': group_id,
##               'prev_id': prev_id,
##               'next_id': next_id,
##               'term_id': term_id}
##    return render(request, 'tracker/circularAplicaciones.html', context)

def maxGroups(term_id):
    if int(term_id) == 1:
        return 5
    elif int(term_id) == 2:
        return 6
    elif int(term_id) == 3:
        return 7
    
def depurate(data):
    result = []
    for item in data:
        l_item = list(item)
        if "www" in l_item[0]:
            strings = l_item[0].split(".")
            string = strings[1]
            l_item[0] = string + ".com"
        word = re.findall(r'\w+\.\w+', l_item[0])
        if len(word) > 0:
            l_item[0] = word[-1]
        result.append(l_item)
    return result
    
def groupSelector(term_id, group_id):
    if int(term_id) == 1:
        if group_id in '1':
            return [22, 26, 28, 34]
        elif group_id in '2':
            return [23, 32, 36, 41]
        elif group_id in '3':
            return [29, 30, 31, 38]
        elif group_id in '4':
            return [27, 37, 39, 40]
        elif group_id in '5':
            return [25, 33, 35, 0]
        else:
            return [22, 26, 28, 34]     
    elif int(term_id) == 2:
        if group_id in '1':
            return [1, 2, 18, 0]
        elif group_id in '2':
            return [4, 10, 22, 0]
        elif group_id in '3':
            return [8, 9, 0, 0]
        elif group_id in '4':
            return [7, 13, 15, 0]
        elif group_id in '5':
            return [5, 17, 0, 0]
        elif group_id in '6':
            return [3, 6, 21, 0]
        else:
            return [1, 2, 18, 0]
    elif int(term_id) == 3:
        if group_id in '1':
            return [1, 2, 3, 0]
        elif group_id in '2':
            return [4, 5, 6, 7]
        elif group_id in '3':
            return [8, 9, 10, 11]
        elif group_id in '4':
            return [12, 13, 14, 15]
        elif group_id in '5':
            return [16, 0, 0, 0]
        elif group_id in '6':
            return [17, 18, 19, 20]
        elif group_id in '7':
            return [21, 22, 23, 24]
        else:
            return [1, 2, 3, 0]

def getNames(list_of_users, term):
    users = Users.objects.filter(termID=term)
    names = []
    for item in users:
        if item.id in list_of_users:
            names.append(item.first_name + " " + item.last_name)
    while len(names) < 4:
        names.append("-")
    return names

def getNextPrevious(term_id, group_id):
    current = int(group_id)
    if int(term_id) == 1:
        groups = [x for x in range(1, 6)]
    elif int(term_id) == 2:
        groups = [x for x in range(1, 7)]
    elif int(term_id) == 3:
        groups = [x for x in range(1, 8)]
    n = len(groups)
    return [str(groups[(current - 2) % n]), str(groups[(current) % n])]

def getAppList(list_of_app_index):
    new_list = ["" for i in range(len(list_of_app_index))]
    for i in range(len(list_of_app_index)):
        name = Application.objects.filter(id=list_of_app_index[i])[0].application
        if  "Sistema operativo" in name:
            name = "Windows Explorer"
        new_list[i] = name
    return new_list

def depurateTimes(dates_set, sorted_dates, sorted_times):
    new_times = [0 for item in range(0, len(dates_set))]
    for i in range(0, len(dates_set)):
        if dates_set[i] in sorted_dates:
            index = sorted_dates.index(dates_set[i])
            new_times[i] = sorted_times[index]
    return new_times

def strToDate(date_str):
    list_of_strings = date_str.split("-")
    return date(int(list_of_strings[0]), int(list_of_strings[1]), int(list_of_strings[2]))

def classifyUsefullness(dataset):
    dictionary = {}
    dictionary["useful"] = 0
    dictionary["useless"] = 0
    for item in dataset:
        if item.relevance == 1:
            dictionary["useful"] += (datetime.combine(date.min, item.elapsed_time) - datetime.min).total_seconds()
        else:
            dictionary["useless"] += (datetime.combine(date.min, item.elapsed_time) - datetime.min).total_seconds()
    return dictionary

def fetchDocInfofromUser(dataset, termino, user):
    user_activity = filterByUser(dataset, user)
    if termino == 3:
        user_activity = filterByClass(user_activity, "Documents")
    else:
        user_activity = filterByClass(user_activity, "Applications")
    user_activity = filterByRelevance(user_activity, 1)
    return user_activity

def fetchAllDocInfofromUser(dataset, termino, user):
    user_activity = filterByUser(dataset, user)
    if termino == 3:
        user_activity = filterByClass(user_activity, "Documents")
    else:
        user_activity = filterByClass(user_activity, "Applications")
    return user_activity

def fetchAppInfofromUser(dataset, termino, user):
    user_activity = filterByUser(dataset, user)
    user_activity = filterByClass(user_activity, "Applications")
    return user_activity

def buildAppMatrix(activity_list):
    dict_app = {}
    app_list = [0 for i in range(len(activity_list))]
    matrix = []
    
    for i in range(len(activity_list)):
        app_list[i] = activity_list[i].applicationID

    cont = 0
    dict_app, cont = getAppByID(app_list, dict_app, 4, cont)  #Chrome
    dict_app, cont = getAppByID(app_list, dict_app, 652, cont) #Firefox
    dict_app, cont = getAppByID(app_list, dict_app, 100, cont)  #Notepad++
    dict_app, cont = getAppByID(app_list, dict_app, 1161, cont)  #Sublime Text
    dict_app, cont = getAppByID(app_list, dict_app, 36, cont)   #Sublime Text 2
    dict_app, cont = getAppByID(app_list, dict_app, 2247, cont) #Notepad
    dict_app, cont = getAppByID(app_list, dict_app, 29, cont)    #Mintty
    dict_app, cont = getAppByID(app_list, dict_app, 62, cont)    #Github Desktop
                
    for i in range(len(app_list)):
        if app_list[i] not in dict_app:
            dict_app[app_list[i]] = cont
            cont += 1
            
    for i in range(len(list(dict_app.keys()))):
        matrix.append([])
        matrix[i] = [0 for j in range(len(list(dict_app.keys())))]

    for i in range(len(app_list)):
        current = app_list[i]
        next_one = current
        if (i + 1) < len(app_list):
            next_one = app_list[i + 1]

        matrix_i = dict_app[current]
        matrix_j = dict_app[next_one]

        matrix[matrix_i][matrix_j] += 1
    
    return matrix, list(dict_app.keys())

def getAppByID(app_list, dictionary, id_value, cont):
    tmp = cont
    for i in range(len(app_list)):
        if app_list[i] not in dictionary:
            if app_list[i] == id_value:
                dictionary[app_list[i]] = cont
                cont += 1
                break

##    if tmp == cont:
##        cont += 1
    return dictionary, cont
    
##def buildActMatrix(activity_list):
##    dict_app = {}
##    app_list = [0 for i in range(len(activity_list))]
##    matrix = []
##    
##    for i in range(len(activity_list)):
##        app_list[i] = activity_list[i].applicationID
##
##    cont = 0
##    for i in range(len(app_list)):
##        if app_list[i] not in dict_app:
##            dict_app[app_list[i]] = cont
##            cont += 1
##
##    for i in range(len(list(dict_app.keys()))):
##        matrix.append([])
##        matrix[i] = [0 for j in range(len(list(dict_app.keys())))]
##
##    for i in range(len(app_list)):
##        current = app_list[i]
##        next_one = current
##        if (i + 1) < len(app_list):
##            next_one = app_list[i + 1]
##
##        matrix_i = dict_app[current]
##        matrix_j = dict_app[next_one]
##
##        matrix[matrix_i][matrix_j] += 1
##
##    return matrix
        
def buildDataset(activity_list):
    dictionary = {}
    for item in activity_list:
        if item.start_date not in dictionary:
            dictionary[item.start_date] = (datetime.combine(date.min, item.elapsed_time) - datetime.min).total_seconds()
        else:
            dictionary[item.start_date] += (datetime.combine(date.min, item.elapsed_time) - datetime.min).total_seconds()
    sorted_dates = sorted(dictionary)
    time_per_date = []
    for i in range(0, len(sorted_dates)):
        time_per_date.append(dictionary[sorted_dates[i]])
    return sorted_dates, time_per_date

def getTopActivitiesCircular(activity_list):
    dictionary_uful = {}
    dictionary_uless = {}
    dict_uful = {}
    dict_uless = {}
    list_uful = []
    list_uless = []
    l_uful = []
    l_uless = []
    for item in activity_list:
        if item.relevance == 1:
            if item.applicationID not in dictionary_uful:
                dictionary_uful[item.applicationID] = (datetime.combine(date.min, item.elapsed_time) - datetime.min).total_seconds()
            else:
                dictionary_uful[item.applicationID] += (datetime.combine(date.min, item.elapsed_time) - datetime.min).total_seconds()
        else:
            if item.applicationID not in dictionary_uless:
                dictionary_uless[item.applicationID] = (datetime.combine(date.min, item.elapsed_time) - datetime.min).total_seconds()
            else:
                dictionary_uless[item.applicationID] += (datetime.combine(date.min, item.elapsed_time) - datetime.min).total_seconds()

    list_uful = list(dictionary_uful.keys())
    list_uless = list(dictionary_uless.keys())

    l_uful = ["" for i in range(len(list_uful))]
    l_uless = ["" for i in range(len(list_uless))]

    for i in range(len(list_uful)):
        app_name = Application.objects.filter(id=list_uful[i])[0].application
        l_uful[i] = app_name

    for i in range(len(list_uless)):
        app_name = Application.objects.filter(id=list_uless[i])[0].application
        l_uless[i] = app_name

    for i in range(len(list_uful)):
        dict_uful[l_uful[i]] = dictionary_uful[list_uful[i]]

    for i in range(len(list_uless)):
        dict_uless[l_uless[i]] = dictionary_uless[list_uless[i]]
        
    return Counter(dict_uful).most_common(5), Counter(dict_uless).most_common(5)
    
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
    s_date = strToDate(date_start)
    e_date = strToDate(date_end)
    for item in objects:
        if item.start_date >= s_date and item.end_date <= e_date:
            result.append(item)
    return result

def filterByUser(objects, user):
    result = []
    for item in objects:
        if item.userID == user:
            result.append(item)
    return result

def filterByClass(objects, class_object):
    result = []
    if "Doc" in class_object:
        gChromeID = Application.objects.filter(application="Google Chrome")[0].id
    else:
        gChromeID = -1
    class_typeID = Class_Type.objects.filter(class_name=class_object)[0].id
    for item in objects:
        if item.applicationID == gChromeID:
            continue
        else:
            if item.classID == class_typeID:
                result.append(item)
    return result

def filterByRelevance(objects, relevance):
    result = []
    for item in objects:
        if item.relevance == relevance:
            result.append(item)
    return result


