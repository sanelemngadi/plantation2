# Generated by Django 4.2.6 on 2023-10-30 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_remove_plantationordermodel_order_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantationordermodel',
            name='has_driver',
            field=models.BooleanField(default=False),
        ),
    ]
