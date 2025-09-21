from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib import messages

def add_product(request):
    if request.user.role != 'vendor':
         messages.error(request, 'You are not allowed Here')
         return redirect('products-list')

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user
            product.save()
            return redirect('products-list')
    else:
            form = ProductForm()
    return render(request, 'products/add_product.html', {'form':form})

def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/product_list.html', context)