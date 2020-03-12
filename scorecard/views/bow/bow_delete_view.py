from django.views.generic.edit import DeleteView
from django.utils import timezone
from scorecard.models import Bow
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from scorecard.forms.bow import BowUpdateForm
from django.shortcuts import render, redirect
import base64

class BowDeleteView(LoginRequiredMixin, DeleteView):
    model = Bow
    title = 'Delete Bow'
    template_name = 'scorecard/bow/bow_delete.html'
    
    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context 

    def get_success_url(self):
        return reverse_lazy('bow-list')