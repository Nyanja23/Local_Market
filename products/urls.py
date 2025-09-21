from django.urls import path
from . import views

urlpatterns  = [
    path('add-product/', views.add_product, name='add-product'),
    path('products-list/',views.products_list, name='products-list'),
]