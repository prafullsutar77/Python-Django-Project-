from django.db import models

# Create your models here.
class MensWearModel(models.Model):
    modelname=models.CharField(max_length=25)
    modelbrand=models.CharField(max_length=25)
    modelprice=models.FloatField()
    modelqnty=models.IntegerField()

class WomenWearModel(models.Model):
    modelname=models.CharField(max_length=25)
    modelbrand=models.CharField(max_length=25)
    modelprice=models.FloatField()
    modelqnty=models.IntegerField()

class KidsWearModel(models.Model):
    modelname=models.CharField(max_length=25)
    modelbrand=models.CharField(max_length=25)
    modelprice=models.FloatField()
    modelqnty=models.IntegerField()


