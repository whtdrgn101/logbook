from django.views.generic.edit import DeleteView
from django.utils import timezone
from scorecard.models import Round
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from scorecard.forms.bow import BowCreateForm
from django.shortcuts import render, redirect
import base64

class RoundDeleteView(LoginRequiredMixin, DeleteView):
    model = Round
    title = 'Delete Round'
    template_name = 'scorecard/round/round_delete.html'
    
    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context 

    def get_success_url(self):
        log_entry_id = self.request.session.get('active_log_entry_id', None)
        return reverse_lazy('log-entry-detail', kwargs={'pk': log_entry_id})