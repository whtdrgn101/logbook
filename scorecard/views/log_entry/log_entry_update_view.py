from django.views.generic.edit import UpdateView
from django.utils import timezone
from scorecard.models import LogEntry, Bow
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
import base64

class LogEntryUpdateView(LoginRequiredMixin, UpdateView):
    model = LogEntry
    title = 'Update Log Entry'
    fields = ['log_entry_date', 'log_notes', 'bow']
    template_name = 'scorecard/log-entry/logentry_create_update.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context

    def form_valid(self, form):        
        log = form.save()
        log.save()
        return redirect(reverse_lazy('log-entry-detail', kwargs={'pk': log.id}))