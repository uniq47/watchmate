# Generated by Django 3.2a1 on 2023-09-30 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0004_auto_20230927_0951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='avtive',
            new_name='active',
        ),
    ]
