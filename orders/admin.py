from django.contrib import admin
from .models import Order, OrderProduct

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'date_created','complete_status')
    search_fields = ('customer','product')

@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity')
    search_fields= ('order', 'product', 'quantity')