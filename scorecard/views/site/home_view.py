from django.views.generic.base import TemplateView
from django.utils import timezone

class HomeView(TemplateView):

    title = 'Home'
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['title'] = self.title
        return context 