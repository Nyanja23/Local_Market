from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, OrderProduct
from products.models import Product
from django.contrib import messages

def confirm_order(request, pk):
    product = get_object_or_404(Product, id = pk)
    referer = request.META.get("HTTP_REFERER", '/')
    previous_url = request.GET.get('next', referer)
    context = {'product':product, 'referer':previous_url}
    return render(request, 'orders/confirm_order.html', context)


def place_order(request, pk):
    if request.method ==  'POST':
        customer = request.user
        product = get_object_or_404(Product, id = pk)
        quantity = int(request.POST.get('quantity', 1))

        order, created = Order.objects.get_or_create(customer=customer)
        if created:
            messages.success(request, 'Order Placed Successfully')
        else:
            messages.error(request, "Order Already Exists")
            # return render(request,'products/product_list.html')

        order_product, created_order_product = OrderProduct.objects.get_or_create(order = order, product = product, quantity = quantity)

        if not created_order_product:
            messages.error(request, 'Item Already there')
            # return render(request,'products/product_list.html')
        
        messages.success(request, f"You have ordered {quantity} for {product.name}")

        return redirect('home')
    return redirect('products-list')

def get_orders(request):
    products_ordered = OrderProduct.objects.filter(product__vendor = request.user)
    context = {'products':products_ordered}
    print(products_ordered)
    return render(request, 'orders/products_ordered.html', context)

def my_orders(request):
    orders = OrderProduct.objects.filter(order__customer = request.user)
    context = {'orders': orders}

    return render(request, 'orders/my_orders.html', context)
