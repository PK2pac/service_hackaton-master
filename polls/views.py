import csv
from datetime import time, datetime
import pandas as pd

from django.core import serializers
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .forms import *
# Create your views here.
#import jsonpickle


def index(request):
    contests = Contest.objects.all()

    context = {
        'contest_list': contests
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

def chooseCategory(request, id):
    cat_id = request.GET.get('id')
    print(cat_id)

    if id == 0:
        contests = Contest.objects.all()
        print('id == 0 print contests=', contests)

    json = serializers.serialize('json', list(contests))
    print(contests)
    return HttpResponse(json, content_type="application/json")


@csrf_exempt
def addData(request):
    #f = open('./polls/dataset.csv', 'r', encoding='utf-8')
    data = pd.read_csv('./polls/dataset.csv', delimiter=';', encoding='utf-8')
    for index, row in data.iterrows():
        #with open(f) as csvfile:
        print('sfhsf4h4ht4h4j4h5446jj4j464j')
        #readCSV = csv.reader(csvfile, delimiter=';')
        #for row in readCSV:
            #print(row[0])
        Contest.objects.create(title=str(row['name']),
                               description=str(row['description']),
                               date_start=datetime.strptime(row['start'], "%d.%m.%Y").date(),
                               date_finish=datetime.strptime(row['finish'], "%d.%m.%Y").date(),
                               category=int(row['category']),
                               coordinates=str(row['coordinates']),
                               site_link=str(row['contacts'])
                               );

    return redirect("index")
