# Generated by Django 3.1.4 on 2020-12-21 20:52

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='metric',
            managers=[
                ('timescale', django.db.models.manager.Manager()),
            ],
        ),
    ]