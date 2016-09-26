# coding: utf-8

from ajax_select import make_ajax_form
from django.contrib import admin

from .models import Event, Race, Time, Yacht


class YachtInline(admin.TabularInline):
    model = Yacht


class EventAdmin(admin.ModelAdmin):
    inlines = [
        YachtInline,
    ]


class TimeInline(admin.TabularInline):
    model = Time
    form = make_ajax_form(Time, {
        'yacht': 'yacht'
    })


class RaceAdmin(admin.ModelAdmin):
    inlines = [
        TimeInline,
    ]


admin.site.register(Event, EventAdmin)
admin.site.register(Race, RaceAdmin)
