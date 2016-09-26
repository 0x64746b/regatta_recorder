# coding: utf-8

from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from . import views

urlpatterns = [
    url(r'^$', views.list_events, name='events'),
    url(_(r'^events/(?P<event_id>\d+)/$'), views.show_results_overview, name='results_overview'),
    url(_(r'^races/(?P<race_id>\d+)/$'), views.show_results_race, name='results_race'),
]