# Generated by Django 3.0 on 2021-03-14 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0007_auto_20210314_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='from_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='to_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
