from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length = 300)
    city = models.CharField(max_length = 300)
    country = models.CharField(max_length = 300)
    created_at = models.DateTimeField(blank = True, null = True)
    objects = models.Manager()

    def __str__(self):
      return str(self.pk) + ': ' + self.name + ', ' + self.city + ', ' + self.country + ', ' + str(self.created_at)
      
class WaterBottle(models.Model):
    sku = models.CharField(max_length = 300)
    brand = models.CharField(max_length = 300)
    cost = models.FloatField()
    size = models.CharField(max_length = 300)
    mouthSize = models.CharField(max_length = 300)
    color = models.CharField(max_length = 300)
    suppliedBy = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    currentQuantity = models.IntegerField()
    objects = models.Manager()

    def __str__(self):
      return str(self.pk) + ': ' + self.sku + ', ' + self.brand + ', ' + str(self.cost) + ', ' + self.size + ', ' + self.mouthSize + ', ' + self.color + ', ' + str(self.suppliedBy.name) + ', ' + str(self.currentQuantity)