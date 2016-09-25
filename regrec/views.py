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


def get_yachts_for_event(request):
    event_id = request.GET.get('event_id')
    if event_id is None:
        return HttpResponse(
            json.dumps({'error': 'no event specified'}),
            status=http.client.BAD_REQUEST,
            content_type='application/json',
        )
    elif event_id == '':
        yachts = Yacht.objects.all()
    else:
        yachts = Yacht.objects.filter(event__id=event_id)

    return HttpResponse(
        json.dumps({'yachts': [(yacht.id, str(yacht)) for yacht in yachts]}),
        content_type='application/json',
    )
