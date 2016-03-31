from django.shortcuts import render, get_object_or_404

from .models import Coworker

# Create your views here.


def index(request):
    coworkers = Coworker.objects.all()
    context = {'coworkers': coworkers}
    return render(request, 'merit_coworkers/index.html', context)


def info(request, coworker_id):
    coworker = get_object_or_404(Coworker, pk=coworker_id)
    context = {'coworker': coworker}
    return render(request, 'merit_coworkers/info.html', context)

