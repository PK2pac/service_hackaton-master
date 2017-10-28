import csv
from datetime import time

from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .forms import *
# Create your views here.
#import jsonpickle


def index(request):
    contests = Contest.objects.all()
    categories = Contest.objects.values('category').distinct()

    context = {
        'contest_list': contests,
        'category_list': categories
    }

    return render(request, "main/index.html", context)


def chooseCategory(request, id):
    cat_id = request.GET.get('id')
    print(cat_id)
    if id == 0:
        contests = Contest.objects.all()
        print('id == 0 print contests=', contests)
        json = serializers.serialize('json', list(contests))
        print(contests)
        return HttpResponse(json, content_type="application/json")
    else:
        contests = Contest.objects.filter(category=cat_id)
        json = serializers.serialize('json', list(contests))
        print(contests)
        return HttpResponse(json, content_type="application/json")


@csrf_exempt
def addData(request):
    if request.method == 'POST':
        form = dataForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            with open(file) as csvfile:
                readCSV = csv.reader(csvfile, delimiter=';')
                for row in readCSV:
                    Contest.objects.create(name=str(row[0]),
                                           description=str(row[1]),
                                           date_start=time.strptime(row[2]),
                                           date_finish=time.strptime(row[3]),
                                           category=int(row[4]),
                                           coordinates=str(row[5]),
                                           site_link=str(row[6])
                                           );

    return redirect("index")
