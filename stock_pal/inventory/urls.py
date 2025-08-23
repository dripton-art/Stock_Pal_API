from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='inventory-home'),
    path('suppliers/', views.suppliers, name='inventory-suppliers'),
    path('product/', views.product, name='inventory-product'),
    path('sales/', views.sales, name='inventory-sales'),
]