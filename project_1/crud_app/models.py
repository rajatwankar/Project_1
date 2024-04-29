from django.db import models

# Create your models here.


class Laptop(models.Model):
    l_id = models.IntegerField(unique=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    ram = models.IntegerField()
    memory = models.IntegerField()
    price = models.FloatField()