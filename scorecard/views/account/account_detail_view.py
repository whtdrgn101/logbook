from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

from scorecard.models import LogEntry, Bow, AccountProfile

class AccountProfileView(LoginRequiredMixin, TemplateView):

    model = AccountProfile
    
    title = 'Account Details'
    template_name = 'account_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['title'] = self.title
        return context