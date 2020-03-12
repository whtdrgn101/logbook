from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

from scorecard.models import LogEntry, Bow, Round

class LogEntryDetailView(LoginRequiredMixin, DetailView):

    model = LogEntry
    paginate_by = 20
    title = 'Log Entry Details'
    template_name = 'scorecard/log-entry/logentry_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['title'] = self.title

        rounds = Round.objects.filter(log_entry_id=context['object'].id)
        context['rounds'] = rounds

        #Save log_entry_id to session state for use updating rounds
        self.request.session['active_log_entry_id'] = context['object'].id

        return context