from django.shortcuts import render, HttpResponseRedirect
from .models import OrderItem
from .forms import OrderCreateForm
# from cart.cart import Cart
from cart.cart import Cart
from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request, 'checkout/confirmation.html', {'order': order, 'cart': cart})
    else:
        form = OrderCreateForm()
    return render(request, 'checkout/checkout.html', {'cart': cart,
                                                      'form': form})
