from django.views.generic.edit import UpdateView
from django.utils import timezone
from scorecard.models import Round, End
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from scorecard.forms.bow import BowCreateForm
from django.shortcuts import render, redirect
import base64

class RoundUpdateView(LoginRequiredMixin, UpdateView):
    model = Round
    title = 'New Round'
    fields = ['score', 'round_type']
    template_name = 'scorecard/round/round_create_update.html'
    
    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = self.title

        ends = End.objects.filter(round_id=context['object'].id)
        context['ends'] = ends

        #Save log_entry_id to session state for use updating rounds
        self.request.session['active_round_id'] = context['object'].id

        return context 

    def form_valid(self, form):
        log_entry_id = self.request.session.get('active_log_entry_id', None)
        if log_entry_id:
            form.instance.log_entry_id = log_entry_id
            round = form.save()
            round.save()
        
        return redirect(reverse_lazy('log-entry-detail', kwargs={'pk': log_entry_id}))