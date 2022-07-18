import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from store.models import Supplier, Yard, cost, grade, metal

@login_required(login_url='login')
def dashboard(request):
    total_product = Yard.objects.count()
    total_supplier = Supplier.objects.count()
    total_buyer = metal.objects.count()
    total_oder = cost.objects.count()
    orders = grade.objects.all()
    context = {
        'product': total_product,
        'supplier': total_supplier,
        'buyer': total_buyer,
        'order': total_oder,
        'orders': orders
    }
    return render(request, 'dashboard.html', context)  
    
