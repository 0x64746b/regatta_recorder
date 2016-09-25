# coding: utf-8

from django.shortcuts import render

from .models import Event


def list_events(request):
    return render(request, 'regrec/events.html', {'events': Event.objects.all()})


def show_results_overview(request, event_id):
    return render(request, 'regrec/overview.html', {'event': Event.objects.get(id=int(event_id))})
