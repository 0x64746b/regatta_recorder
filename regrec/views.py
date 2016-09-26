# coding: utf-8

import http.client
import json

from django.http import HttpResponse
from django.shortcuts import render

from .models import Event, Race, Yacht


def list_events(request):
    return render(request, 'regrec/events.html', {'events': Event.objects.all()})


def show_results_overview(request, event_id):
    return render(request, 'regrec/overview.html', {'event': Event.objects.get(id=int(event_id))})


def show_results_race(request, race_id):
    race = Race.objects.get(id=int(race_id))
    return render(request, 'regrec/race.html', {'event': race.event, 'race': race})
