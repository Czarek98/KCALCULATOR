# Generated by Django 3.2 on 2021-04-21 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kcal', '0002_food_grams'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='carbs',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='fat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='proteins',
            field=models.FloatField(null=True),
        ),
    ]
