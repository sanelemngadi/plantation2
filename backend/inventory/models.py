from django.db import models
from suppliers.models import PlantationSupplier
from products.models import PlantationProduct

# Create your models here.

class PlantationStock(models.Model):
    # supplier = models.ForeignKey(PlantationSupplier, on_delete=models.CASCADE)
    product = models.ForeignKey(PlantationProduct, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} {self.qauntity} for R{self.price}"
    
    def get_total_amount(self):
        return self.quantity * self.product.price