from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

from scorecard.models import LogEntry, Bow

# Create your views here.
class LogEntryListView(LoginRequiredMixin, ListView):

    model = LogEntry
    paginate_by = 20
    title = 'Scorecards'
    template_name = 'scorecard/log-entry/logentry_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['title'] = self.title
        return context