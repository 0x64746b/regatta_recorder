# coding: utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.list_events, name='events'),
    url(r'^(?P<event_id>\d+)/$', views.show_results, name='results'),
]