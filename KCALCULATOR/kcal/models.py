from django.db import models


# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=255)
    kcal = models.FloatField()
    proteins = models.FloatField()
    fat = models.FloatField()
    carbs = models.FloatField()


class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    kcalperday = models.FloatField()
    #food = models.ForeignKey(Food, on_delete=models.CASCADE)




