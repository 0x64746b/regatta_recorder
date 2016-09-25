from django.contrib import admin

from .models import Event, Race, Run, Yacht


class YachtInline(admin.TabularInline):
    model = Yacht


class EventAdmin(admin.ModelAdmin):
    inlines = [
        YachtInline,
    ]


class RunInline(admin.TabularInline):
    model = Run


class RaceAdmin(admin.ModelAdmin):
    inlines = [
        RunInline,
    ]

    class Media:
        js = [
            'regrec/js/jquery-3.1.1.min.js',
            'regrec/js/race_admin.js',
        ]


admin.site.register(Event, EventAdmin)
admin.site.register(Race, RaceAdmin)
