from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

from scorecard.models import LogEntry, Bow

class BowDetailView(LoginRequiredMixin, DetailView):

    model = Bow
    paginate_by = 20
    title = 'Bow Details'
    template_name = 'scorecard/bow/bow_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['title'] = self.title
        return context