from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import View
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

from scorecard.models import LogEntry, Bow

class BowImageView(LoginRequiredMixin, View):

    model = Bow
    
    def get(self, request, **kwargs):
        bow = Bow.objects.get(id=kwargs['pk'])
        return HttpResponse(bow.picture_binary, content_type=bow.picture_type)
    