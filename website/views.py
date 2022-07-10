import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from store.models import Supplier, Yard, cost


@login_required(login_url='login')
def dashboard(request):
    total_supplier = Supplier.objects.count()
    total_yard = Yard.objects.count()
    total_cost = cost.objects.count()
    context = {
        'Supplier': total_supplier,
        'Yard': total_yard,
        'Cost': total_cost
    }
    return render(request, 'dashboard.html', context)

def json_file(request):
    
    return render(request)  
    
