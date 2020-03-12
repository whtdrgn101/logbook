from django.db import models
from .account_profile import AccountProfile
from .bow import Bow

class LogEntry(models.Model):
    log_entry_date = models.DateField()
    log_notes = models.CharField(max_length=255)
    bow = models.ForeignKey(Bow, on_delete=models.CASCADE)
    account = models.ForeignKey(AccountProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.log_entry_date} w/({self.bow.draw_weight}lb {self.bow.make} - {self.bow.model})"