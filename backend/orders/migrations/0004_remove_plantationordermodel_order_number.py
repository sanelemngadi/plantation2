# Generated by Django 4.2.6 on 2023-10-30 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_plantationordermodel_total_grand_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantationordermodel',
            name='order_number',
        ),
    ]
