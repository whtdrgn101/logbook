from django.views.generic import View
from django.utils import timezone
from scorecard.models import Bow
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from scorecard.forms.bow import BowCreateForm
from django.shortcuts import render, redirect
import base64

class BowCreateView(LoginRequiredMixin, View):
    model = Bow
    title = 'New Bow'
    form_class = BowCreateForm
    template_name = 'scorecard/bow/bow_create.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form':form, 'title':self.title})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            bow = Bow()
            bow.name = form.cleaned_data['name']
            bow.make = form.cleaned_data['make']
            bow.model = form.cleaned_data['model']
            bow.year = form.cleaned_data['year']
            bow.bow_type = form.cleaned_data['bow_type']
            bow.draw_weight = form.cleaned_data['draw_weight']
            bow.brace_height_inches = form.cleaned_data['brace_height_inches']
            bow.ata_distance_inches = form.cleaned_data['ata_distance_inches']
            bow.setup_notes = form.cleaned_data['setup_notes']
            bow.stabalizer_setup = form.cleaned_data['stabalizer_setup']
            bow.rest_type = form.cleaned_data['rest_type']
            if len(request.FILES) > 0:
                bow.picture = base64.b64encode(request.FILES['picture'].read()).decode("UTF-8")
                bow.picture_type = request.FILES['picture'].content_type
            bow.account_id = self.request.session.get('account_id', None)
            bow.save()
            return redirect(reverse_lazy('bow-detail', kwargs={'pk': bow.id}))
        else:
            return render(request, self.template_name, {'form':form, 'title':self.title})