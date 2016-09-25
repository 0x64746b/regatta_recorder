# coding: utf-8

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def crop_timedelta(delta):
    return delta.split('.')[0]