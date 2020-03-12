from django.views.generic.edit import UpdateView
from django.utils import timezone
from scorecard.models import End
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
import base64

class EndUpdateView(LoginRequiredMixin, UpdateView):
    model = End
    title = 'Update End'
    fields = ['score']
    template_name = 'scorecard/end/end_create_update.html'
    
    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context 

    def form_valid(self, form):
        round_id = self.request.session.get('active_round_id', None)
        if round_id:
            form.instance.round_id = round_id
            round = form.save()
            round.save()
        
        return redirect(reverse_lazy('round-update', kwargs={'pk': round_id}))