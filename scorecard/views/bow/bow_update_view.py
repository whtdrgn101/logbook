from django.views.generic.edit import UpdateView
from django.utils import timezone
from scorecard.models import Bow
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from scorecard.forms.bow import BowUpdateForm
from django.shortcuts import render, redirect
import base64

class BowUpdateView(LoginRequiredMixin, UpdateView):
    model = Bow
    title = 'Update Bow'
    fields = ['name', 'make', 'model', 'year', 'bow_type', 'draw_weight', 'rest_type', 'cable_material', 'brace_height_inches', 'ata_distance_inches', 'stabalizer_setup', 'setup_notes']
    template_name = 'scorecard/bow/bow_update.html'
    
    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context 

    def form_valid(self, form):        
        bow = form.save()
        bow.save()
        return redirect(reverse_lazy('bow-detail', kwargs={'pk': bow.id}))