from .cart import Cart
from django.contrib.auth.models import User


def cart(request):
    return {'cart': Cart(request)}
