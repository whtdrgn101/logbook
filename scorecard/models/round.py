from django.db import models
from .log_entry import LogEntry

class RoundType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    end_count = models.IntegerField()
    shots_per_end = models.IntegerField()
    max_score_per_show = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

class Round(models.Model):
    score = models.IntegerField()
    log_entry = models.ForeignKey(LogEntry, on_delete=models.CASCADE)
    round_type = models.ForeignKey(RoundType, null=True, on_delete=models.SET_NULL)
