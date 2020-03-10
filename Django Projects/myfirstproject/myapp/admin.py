from django.contrib import admin
from .models import WineProducer, Wine

# Register your models here.
admin.site.register(WineProducer)
admin.site.register(Wine)