from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from shop.models import Products
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib.auth.models import User


# Create your views here.

@require_POST
# @login_required()
def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Products, pk=id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, id):
    cart = Cart(request)
    product = Products.objects.get(pk=id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})
