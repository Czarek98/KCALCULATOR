# Generated by Django 3.2 on 2021-04-21 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kcal', '0003_auto_20210421_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='status',
            field=models.CharField(choices=[('unconfirmed', 'Waiting for confirmed'), ('confirmed', 'Accepted'), ('rejected', 'Rejected')], default='unconfirmed', max_length=40),
        ),
    ]
