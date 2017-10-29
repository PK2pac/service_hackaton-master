import csv
from datetime import time, datetime
import pandas as pd
import json

import vk

import requests
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import polls.test as telegram_test


def index(request):
    contests = Contest.objects.all().order_by('date_start').distinct()
    categories = Contest.objects.order_by().values('category').distinct()
    labels = ['Конкурс', 'Конференция']

    context = {
        'contest_list': contests,
        'category_list': categories,
        'category_label': labels
    }

    return render(request, "main/index.html", context)

"""
for getting title and description for list of dicts
it returns a list of strings
use split() to get title and description, delimiter:',' 
"""
def get_t_d(dict):
    td_list = []
    for i, item in enumerate (dict):
	    
        title = item['fields']['title']
        description = item['fields']['description']
        t_d_string = "%s, %s" % (title, description)
        td_list.append(t_d_string)
    return td_list

def get_t_d(dict):
    td_list = []
    for i, item in enumerate(dict):
        td_list.append({'title': item.title,
                        'description': item.description,
                        'date_start': str(item.date_start),
                        'date_finish': str(item.date_finish),
                        'site_link': item.site_link,
                        'address': item.address})
    return td_list


def chooseCategory(request, id):
    cat_id = request.GET.get('id')
    if int(cat_id) == 9 or int(id) == 9:
        contests = Contest.objects.all().distinct()
        test = json.dumps(get_t_d(contests))
        return HttpResponse(test, content_type="application/json")
    else:
        contests = Contest.objects.filter(category=cat_id).distinct()
        test = json.dumps(get_t_d(contests))
        return HttpResponse(test, content_type="application/json")


@csrf_exempt
def addData(request):
    #f = open('./polls/dataset.csv', 'r', encoding='utf-8')
    data = pd.read_csv('./polls/dataset.csv', delimiter=';', encoding='utf-8')
    for index, row in data.iterrows():
        #with open(f) as csvfile:
        #readCSV = csv.reader(csvfile, delimiter=';')
        #for row in readCSV:
            #print(row[0])
        Contest.objects.create(title=str(row['name']),
                               description=str(row['description']),
                               date_start=datetime.strptime(row['start'], "%d.%m.%Y").date(),
                               date_finish=datetime.strptime(row['finish'], "%d.%m.%Y").date(),
                               category=int(row['category']),
                               coordinates=str(row['coordinates']),
                               site_link=str(row['contacts']),
                               address=str(row['adress'])
                               );


    return redirect("index")


@csrf_exempt
def addContest(request):
    if request.POST['title']:
        title = request.POST['title']
        description = request.POST['descr']
        categ = request.POST['categ']
        start = request.POST['start']
        finish = request.POST['finish']
        link = request.POST['link']
        address = request.POST['address']
        coordinates=""
        Contest.objects.create(title=title,
                               description=description,
                               category=categ[0],
                               date_start=datetime.strptime(start, "%d.%m.%Y").date(),
                               date_finish=datetime.strptime(finish, "%d.%m.%Y").date(),
                               site_link=link,
                               address=address,
                               coordinates=coordinates)

        event = [title,start,finish,address,link ]
        telegram_test.send_newsletter(event)

    return redirect("index")



@csrf_exempt
def vkParsing(request):
    session = vk.Session(access_token='41547da141547da141547da168410a14134415441547da118ea3a43f6cc46a2ea378d09')
    vk_api = vk.API(session, v='5.68')

    mas = vk_api.wall.get(owner_id='-101826369', count=30)

    def get_vk_item(json_data, key):
        text_array = []
        for i, item in enumerate(json_data['items']):
            item_text = item[key]
            text_array.append(item_text)
        return text_array

    info_array = get_vk_item(mas, 'text')
    key_words = ['хакатон']
    clean_info_array = []
    for info in info_array:
        for key_word in key_words:
            if key_word in info:
                clean_info_array.append(info)

    resultFyle = open("vk_data.csv", 'wb')

    # Write data to file
    for r in clean_info_array:
        resultFyle.write(r.encode())
    resultFyle.close()

    return redirect("index")


@csrf_exempt
def webParsing(request):
    res = requests.get("http://portal.tpu.ru/science/konf")
    soup = BeautifulSoup(res.content, 'lxml')

    data = []
    for table_row in soup.select("table.little tr")[5:]:
        col = table_row.find_all("td")
        try:
            if col[1].text != 'Инфомационное сообщение':
                data.append(col[0].text)
                data.append(col[1].text)
        except:
            pass

    resultFyle = open("tpu_website_data.csv", 'wb')

    for r in data:
        resultFyle.write(r.encode())
    resultFyle.close()

    return redirect("index")