from django.shortcuts import render

from .models import Coworker

# Create your views here.


def index(request):
    coworkers = Coworker.objects.all()
    context = {'coworkers': coworkers}
    return render(request, 'merit_coworkers/index.html', context)


def info(request):
    return render(request)

