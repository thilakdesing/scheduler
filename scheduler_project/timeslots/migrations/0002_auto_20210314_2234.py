# Generated by Django 3.0 on 2021-03-14 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeslots', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslots',
            name='from_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='timeslots',
            name='to_time',
            field=models.TimeField(),
        ),
    ]