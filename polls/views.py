from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
# Create your views here.
import jsonpickle


def index(request):
    contests = Contest.objects.all()
    organisations = Organisation.objects.all()
    categories = Category_contest.objects.all()

    context = {
        'contest_list': contests,
        'organisation_list': organisations,
        'category_list': categories
    }

    return render(request, "main/index.html", context)


def chooseCategory(request, id):
    cat_id = request.GET.get('id')
    print(cat_id)

    if id == 0:
        contests = Contest.objects.all()
        print('id == 0 print contests=', contests)
    else:
        print('id =', id)
        cat = Category_contest.objects.filter(id=id)
        print('cat=', cat)
        contests = Contest.objects.filter(category=cat)

    json = serializers.serialize('json', list(contests))
    print(contests)
    return HttpResponse(json, content_type="application/json")
