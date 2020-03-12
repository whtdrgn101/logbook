from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

from scorecard.models import LogEntry, Bow

class BowListView(LoginRequiredMixin, ListView):

    model = Bow
    paginate_by = 8
    title = 'Bows'
    template_name = 'scorecard/bow/bow_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['title'] = self.title
        return context