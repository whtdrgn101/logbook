from django.contrib import admin
from .models import BowType, RoundType

# Register your models here.
admin.site.register(RoundType)
admin.site.register(BowType)