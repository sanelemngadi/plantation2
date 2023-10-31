from django.db import models
# from services.models import PlantationService
# from django.contrib.auth.models import User
from suppliers.models import PlantationSupplier

# Create your models here.
class PlantationProduct(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    # service = models.ForeignKey(PlantationService, on_delete=models.CASCADE, related_name="products")
    date = models.DateField(auto_now_add=True)
    rent_price = models.FloatField(default=0.0)
    available = models.BooleanField(default=True)
    # stock = models.IntegerField(default=1)
    # discount_percentage = models.IntegerField(default=0)
    discount_percentage = models.IntegerField(default=0)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    supplier = models.ForeignKey(PlantationSupplier, on_delete=models.CASCADE, related_name="products")
    quantity = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        ordering = ("-date",)

    def buy(self, quantity): # when we buy we subtract from stock and email the admin that we dont have no more stock
        self.quantity -= quantity
        self.save()
        
    def add_stock(self, quantity):
        self.quantity += quantity
        self.save()

    def __str__(self):
        return self.name