# Generated by Django 4.2.6 on 2023-10-28 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantationappointmentsmodel',
            name='fumigation_area',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='plantationappointmentsmodel',
            name='price_per_sqm',
            field=models.FloatField(),
        ),
    ]
