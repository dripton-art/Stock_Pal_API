from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'inventory/home.html')

def suppliers(request):
    return render(request, 'inventory/suppliers.html')

def product(request):
    return render(request, 'inventory/product.html')

def sales(request):
    return render(request, 'inventory/sales.html')
