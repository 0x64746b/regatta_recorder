# coding: utf-8

from ajax_select import register, LookupChannel
from django.db.models import Q

from .models import Yacht

@register('yacht')
class YachtLookup(LookupChannel):

    model = Yacht

    def get_query(self, query, request):
        return self.model.objects.filter(
            Q(name__icontains=query) |
            Q(event__name__icontains=query) |
            Q(skipper__icontains=query) |
            Q(model__icontains=query)
        )
