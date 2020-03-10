from django.db import models
from django.utils import timezone
# Create your models here.

class WineProducer(models.Model):
	name = models.CharField(max_length = 300)
	country = models.CharField(max_length = 300)
	created_at = models.DateTimeField(blank = True, null = True)
	objects = models.Manager()

	def __str__(self):
		return str(self.pk) + ': ' + self.name + ', ' + self.country

class Wine(models.Model):
	name = models.CharField(max_length = 300)
	vintage = models.CharField(max_length = 300)
	created_at = models.DateTimeField(blank = True, null = True)
	wineProducer = models.ForeignKey(WineProducer, on_delete=models.CASCADE)
	objects = models.Manager()

	def __str__(self):
		return str(self.pk) + ': ' + self.name + ', ' + self.vintage + ', ' + str(self.wineProducer)