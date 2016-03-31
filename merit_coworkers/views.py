from django.shortcuts import render
from django.http import Http404

from .models import Coworker

# Create your views here.


def index(request):
    coworkers = Coworker.objects.all()
    context = {'coworkers': coworkers}
    return render(request, 'merit_coworkers/index.html', context)


def info(request, coworker_id):
    try:
        coworker = Coworker.objects.get(pk=coworker_id)
    except Coworker.DoesNotExists:
        raise Http404("Coworker does not exists")
    context = {'coworker': coworker}
    return render(request, 'merit_coworkers/info.html', context)

