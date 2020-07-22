from django.db import models
from .account_profile import AccountProfile

class BowType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    
    def __str__(self):
        return f"{self.name}"

class Bow(models.Model):
    name = models.CharField(max_length=100)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=150)
    year = models.IntegerField()
    bow_type = models.ForeignKey(BowType, null=True, on_delete=models.SET_NULL)
    draw_weight = models.FloatField()
    brace_height_inches = models.FloatField(null=True)
    ata_distance_inches = models.FloatField(null=True)
    cable_material = models.CharField(max_length=50, null=True)
    stabalizer_setup = models.TextField(null=True)
    rest_type = models.CharField(null=True, max_length=2, choices = [('BL', 'Blade'), ('DA', 'Drop Away'), ('WB', 'Whicker-Biscuit')], default='BL')
    setup_notes = models.TextField(null=True)
    picture = models.TextField(null=True)
    picture_binary = models.BinaryField(null=True)
    picture_type = models.CharField(null=True, max_length=25)
    account = models.ForeignKey(AccountProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.draw_weight}lb {self.make} - {self.model})"