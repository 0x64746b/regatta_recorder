# coding: utf-8

from datetime import timedelta

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Event(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')

    def __str__(self):
        return self.name


class Race(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='races')
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = _('race')
        verbose_name_plural = _('races')

    def __str__(self):
        return _('{race} of {event}').format(race=self.name, event=self.event)


class Yacht(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='yachts', verbose_name=_('event'))
    name = models.CharField(max_length=128, verbose_name=_('name'))
    model = models.CharField(max_length=128, verbose_name=_('model'))
    yardstick = models.PositiveSmallIntegerField(verbose_name=_('yardstick'))
    skipper = models.CharField(max_length=128, verbose_name=_('skipper'))

    class Meta:
        verbose_name = _('yacht')
        verbose_name_plural = _('yachts')

    @property
    def result(self):
        result = timedelta()

        for time in self.times.all():
            result += time.yardstick_time

        return result

    def __str__(self):
        return _('{yacht} at {event}').format(yacht=self.name, event=self.event)


class Time(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='times', verbose_name=_('race'))
    yacht = models.ForeignKey(Yacht, on_delete=models.CASCADE, related_name='times', verbose_name=_('yacht'))
    start_time = models.DateTimeField(verbose_name=_('start time'))
    finish_time = models.DateTimeField(verbose_name=_('finish time'))
    note = models.CharField(max_length=128, blank=True, null=True, verbose_name=_('note'))

    class Meta:
        verbose_name = _('time')
        verbose_name_plural = _('times')

    @property
    def duration(self):
        return self.finish_time - self.start_time

    @property
    def yardstick_time(self):
        return self.duration * 100 / self.yacht.yardstick

    def __str__(self):
        return _('{yacht} in {race}').format(yacht=self.yacht.name, race=self.race)
