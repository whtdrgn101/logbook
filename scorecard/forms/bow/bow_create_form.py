from django import forms
from scorecard.models import BowType

class BowCreateForm(forms.Form):
    picture = forms.FileField(label="Picture", help_text="Max 2MB", required=False)
    name = forms.CharField(label="Name", max_length=100, required=True)
    make = forms.CharField(label="Make", max_length=50, required=True)
    model = forms.CharField(label="Model", max_length=150, required=True)
    year = forms.IntegerField(label="Year", required=False)
    bow_type = forms.ModelChoiceField(queryset=BowType.objects.all())
    draw_weight = forms.FloatField(label="Draw Weight/lbs")
    brace_height_inches = forms.FloatField(label="Brace Height/in", required=False)
    ata_distance_inches = forms.FloatField(label="Axel to Axel Distance/in", required=False)
    cable_material = forms.CharField(label="Cable Material", max_length=50, required=False)
    rest_type = forms.ChoiceField(label="Rest Type", required=False, choices = [('BL', 'Blade'), ('DA', 'Drop Away'), ('WB', 'Whicker-Biscuit')])
    stabalizer_setup = forms.CharField(widget=forms.Textarea, label="Stabalizer Setup", required=False)
    setup_notes = forms.CharField(widget=forms.Textarea, label="Setup Notes", required=False)
