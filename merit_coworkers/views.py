from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Coworker

# Create your views here.


def index(request):
    coworkers = Coworker.objects.all()
    template = loader.get_template('merit_coworkers/index.html')
    context = {
        'coworkers': coworkers,
    }
    return HttpResponse(template.render(context, request))


def info(request, coworker_id):
    return HttpResponse("Info about %s." % coworker_id)

