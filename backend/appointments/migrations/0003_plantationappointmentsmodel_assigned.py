# Generated by Django 4.2.6 on 2023-10-28 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_alter_plantationappointmentsmodel_fumigation_area_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantationappointmentsmodel',
            name='assigned',
            field=models.BooleanField(default=False),
        ),
    ]