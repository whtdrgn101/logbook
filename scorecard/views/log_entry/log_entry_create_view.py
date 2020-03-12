from django.views.generic.edit import CreateView
from django.utils import timezone
from scorecard.models import LogEntry, Bow
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
import base64

class LogEntryCreateView(LoginRequiredMixin, CreateView):
    model = LogEntry
    title = 'Update Log Entry'
    fields = ['log_entry_date', 'log_notes', 'bow']
    template_name = 'scorecard/log-entry/logentry_create_update.html'

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context

    def form_valid(self, form):        
        form.instance.account_id = self.request.session.get('account_id', None)
        log = form.save()
        log.save()
        return redirect(reverse_lazy('log-entry-detail', kwargs={'pk': log.id}))