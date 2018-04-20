from django.db import models

# Create your models here.
class Cuisine(models.Model):
    label = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
