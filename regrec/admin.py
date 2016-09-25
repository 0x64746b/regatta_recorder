from django.contrib import admin

from .models import Event, Race, Run, Yacht

admin.site.register(Event)
admin.site.register(Race)
admin.site.register(Run)
admin.site.register(Yacht)
