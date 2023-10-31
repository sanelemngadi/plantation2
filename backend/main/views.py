from django.shortcuts import render, get_object_or_404, redirect
# from services.models import PlantationService
# from main.forms import PlantationProductForm, PlantationServiceForm
from django.contrib.auth.decorators import login_required
# Create your views here.

from delivery.models import PlantationDelivery

from products.models import PlantationProduct
from suppliers.models import PlantationSupplier

from user import queries


def index(request):
    products = PlantationProduct.objects.all()
    suppliers = PlantationSupplier.objects.count()

    total_stocks = 0
    for product in products:
        total_stocks += product.quantity

    context = { 
        "products": products, "suppliers": suppliers,
         "total_stocks": total_stocks
    }


    if request.user.is_authenticated:
        settled_deliveries = PlantationDelivery.objects.filter(settled = True).filter(driver = request.user).count()
        not_settled_deliveries = PlantationDelivery.objects.filter(settled = False).filter(driver = request.user).count()

        if queries.is_admin(request.user) or queries.is_superuser(request.user):
            settled_deliveries = PlantationDelivery.objects.filter(settled = True).count()
            not_settled_deliveries = PlantationDelivery.objects.filter(settled = False).count()
        
        context["settled_deliveries"] = settled_deliveries
        context["not_settled_deliveries"] = not_settled_deliveries

    # if request.user.is_authenticated and  

    # context = { 
    #     "products": products, "suppliers": suppliers,
    #     "settled_deliveries": settled_deliveries, 
    #     "not_settled_deliveries": not_settled_deliveries,
    # }
    
    return render(request, "main.html", context)
