# Generated by Django 3.0 on 2021-03-14 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='from_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='appointments',
            name='to_date',
            field=models.DateField(null=True),
        ),
    ]