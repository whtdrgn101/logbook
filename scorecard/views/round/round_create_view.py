from django.views.generic.edit import CreateView
from django.utils import timezone
from scorecard.models import Round
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from scorecard.forms.bow import BowCreateForm
from django.shortcuts import render, redirect
import base64

class RoundCreateView(LoginRequiredMixin, CreateView):
    model = Round
    title = 'New Round'
    fields = ['score', 'round_type']
    template_name = 'scorecard/round/round_create_update.html'
    
    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context 

    def form_valid(self, form):
        log_entry_id = self.request.session.get('active_log_entry_id', None)
        if log_entry_id:
            form.instance.log_entry_id = log_entry_id
            round = form.save()
            round.save()
        
        return redirect(reverse_lazy('log-entry-detail', kwargs={'pk': log_entry_id}))