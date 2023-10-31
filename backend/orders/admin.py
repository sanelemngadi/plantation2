from django.contrib import admin
from orders.models import PlantationOrderModel, PlantationAddress

# Register your models here.

admin.site.register(PlantationOrderModel)
admin.site.register(PlantationAddress)