from django.db import models

# Create your models here.
class LaptopModel(models.Model):
    modelname=models.CharField(max_length=25)
    modelprice=models.FloatField()
    modelqnty=models.IntegerField()

class MobileModel(models.Model):
    modelname=models.CharField(max_length=25)
    modelprice=models.FloatField()
    modelqnty=models.IntegerField()

class TvModel(models.Model):
    modelname=models.CharField(max_length=25)
    modelprice=models.FloatField()
    modelqnty=models.IntegerField()

