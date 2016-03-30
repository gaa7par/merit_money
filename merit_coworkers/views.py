from django.shortcuts import render
from django.http import HttpResponse

from .models import Coworker

# Create your views here.


def index(request):
    coworkers = Coworker.objects.all()
    first_name = [name.first_name for name in coworkers]
    last_name = [name.last_name for name in coworkers]
    output = first_name + [' '] + last_name
    return HttpResponse(output)


def info(request, coworker_id):
    return HttpResponse("Info about %s." % coworker_id)

