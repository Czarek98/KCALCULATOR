from django.db import models

IsAccepted_STATUS = (
    (
        ('unconfirmed', 'Waiting for confirmed'),
        ('confirmed', 'Accepted'),
        ('rejected', 'Rejected')
    )
)
IsFoodOrDrink = (
    (
        ('jedzenie', 'food'),
        ('napój', 'drink')
    )
)


# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    kcalperday = models.FloatField()


class Food(models.Model):
    name = models.CharField(max_length=255)
    grams = models.FloatField(default=100.0)
    kcal = models.FloatField()
    proteins = models.FloatField(null=True)
    fat = models.FloatField(null=True)
    carbs = models.FloatField(null=True)
    status = models.CharField(choices=IsAccepted_STATUS, default='unconfirmed', max_length=40)
    DrinkOrFood = models.CharField(choices=IsFoodOrDrink, default='jedzenie', max_length=40)
    ownerOfFood = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name



    # food = models.ForeignKey(Food, on_delete=models.CASCADE)
