# Generated by Django 4.2.6 on 2023-10-30 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantationdelivery',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deliveries', to=settings.AUTH_USER_MODEL),
        ),
    ]
