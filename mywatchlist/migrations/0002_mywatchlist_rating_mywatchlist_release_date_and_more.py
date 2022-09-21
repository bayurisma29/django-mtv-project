# Generated by Django 4.1 on 2022-09-21 04:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mywatchlist',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mywatchlist',
            name='release_date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='mywatchlist',
            name='watched',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='mywatchlist',
            name='review',
            field=models.TextField(blank=True),
        ),
    ]