
from django.shortcuts import render
from .models import Product

def product_list(request):
    context = {
        'name': 'Rizki Amani Hasanah',  
        'npm': '2306213376', 
        'class_name': 'PBP B',  
    }

    return render(request, 'main.html', context)
