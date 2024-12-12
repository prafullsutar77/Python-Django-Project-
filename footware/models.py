from django.db import models

# Create your models here.
class ShoesModel(models.Model):
    modelname=models.CharField(max_length=25)
    modelcolor=models.CharField(max_length=10)
    modelsize=models.FloatField()
    modelprice=models.IntegerField()
    modelqnty=models.IntegerField()

class SliperModel(models.Model):
    modelname=models.CharField(max_length=25)
    modelcolor=models.CharField(max_length=10)
    modelsize=models.FloatField()
    modelprice=models.IntegerField()
    modelqnty=models.IntegerField()

class SportsModel(models.Model):
    modelname=models.CharField(max_length=25)
    modelcolor=models.CharField(max_length=10)
    modelsize=models.FloatField()
    modelprice=models.IntegerField()
    modelqnty=models.IntegerField()

