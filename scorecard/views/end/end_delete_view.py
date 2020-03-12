from django.views.generic.edit import DeleteView
from django.utils import timezone
from scorecard.models import End
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
import base64

class EndDeleteView(LoginRequiredMixin, DeleteView):

    model = End
    title = 'Delete Bow'
    template_name = "scorecard/end/end_delete.html"

    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context 

    def get_success_url(self):
        round_id = self.request.session.get('active_round_id', None)
        return reverse_lazy('round-update', kwargs={'pk': round_id})