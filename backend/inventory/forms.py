from django import forms
from inventory.models import PlantationStock

class PlantationStockForm(forms.ModelForm):
    class Meta:
        model = PlantationStock
        fields = "__all__"