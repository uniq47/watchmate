# Generated by Django 3.2a1 on 2023-09-27 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0003_auto_20230925_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='number_of_ratings',
            field=models.IntegerField(default=0),
        ),
    ]
