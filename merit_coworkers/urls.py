from django.conf.urls import url

from . import views

app_name = 'merit_coworkers'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<coworker_id>[0-9]+)/info/$', views.info, name='info'),
    url(r'^(?P<coworker_id>[0-9]+)/give_kudo/$', views.give_kudo, name='give_kudo'),
    url(r'^(?P<coworker_id>[0-9]+)/results/$', views.results, name='results'),
]

