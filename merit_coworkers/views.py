from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Merit Coworkers")


def info(request, coworker_id):
    return HttpResponse("Info about %s." % coworker_id)

