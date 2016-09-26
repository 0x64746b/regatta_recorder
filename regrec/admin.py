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


class RaceAdmin(admin.ModelAdmin):
    inlines = [
        TimeInline,
    ]


admin.site.register(Event, EventAdmin)
admin.site.register(Race, RaceAdmin)
