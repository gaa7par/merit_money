from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Coworker, Kudo

# Create your views here.


def index(request):
    coworkers = Coworker.objects.all()
    context = {'coworkers': coworkers}
    return render(request, 'merit_coworkers/index.html', context)


def info(request, coworker_id):
    coworker = get_object_or_404(Coworker, pk=coworker_id)
    context = {'coworker': coworker}
    return render(request, 'merit_coworkers/info.html', context)


def give_kudo(request, coworker_id):
    coworker = get_object_or_404(Coworker, pk=coworker_id)
    context = {
        'coworker': coworker,
        'error_message': "You didn't give a kudo.",
    }

    try:
        selected_kudo = coworker.kudo_set.get(pk=request.POST['kudo'])
    except (KeyError, Kudo.DoesNotExist):
        return render(request, 'merit_coworkers/info.html', context)
    else:
        selected_kudo.kudos += 1
        selected_kudo.save()
        return HttpResponseRedirect(reverse('merit_coworkers:results', args=(coworker.id,)))


def results(request, coworker_id):
    coworker = get_object_or_404(Coworker, pk=coworker_id)
    context = {'coworker': coworker}
    return render(request, 'merit_coworkers/results.html', context)

