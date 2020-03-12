from django.db import models
from .round import Round

class End(models.Model):
    score = models.IntegerField()
    round = models.ForeignKey(Round, on_delete=models.CASCADE)