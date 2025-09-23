from django.urls import path
from . import views

urlpatterns = [
    path('make-order/<int:pk>/', views.place_order, name='order-product'),
    path('confirm-order/<int:pk>/', views.confirm_order, name='confirm-order'),
    path('ordered-products', views.get_orders, name='ordered-products'),
    path('my-orders/', views.my_orders, name='my-orders'),
]