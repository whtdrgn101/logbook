from django.db import models
from django.contrib.auth.models import User

class AccountProfile(models.Model):
    last_login_date = models.DateField(null = True)
    account_user = models.ForeignKey(User, on_delete=models.CASCADE)