from django.shortcuts import render, get_object_or_404
from .models import Category, Products, SubCategory
from django.core.paginator import Paginator
from cart.forms import CartAddProductForm


# Create your views here.

def index(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    products = Products.objects.all()
    paginator = Paginator(products, 5)
    page = request.GET.get('page')
    p = paginator.get_page(page)
    cart_product_form = CartAddProductForm()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=categories)
    context = {
        'products': products,
        'categories': categories,
        'category': category,
        'subcategories': subcategories,
        'p': p,
        'cart_product_form': cart_product_form,
        'index': 'active',
    }
    return render(request, 'shop/index.html', context)


def product_detail(request, category, subcategory, id):
    product = Products.objects.get(pk=id)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'shop/detail.html', context)


def products(request, category, subcategory):
    product = Products.objects.all()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    context = {
        'product': product,
        'categories': categories,
        'subcategories': subcategories,
    }
    return render(request, 'shop/products.html', context)


def shop(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    products = Products.objects.all()
    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    p = paginator.get_page(page)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Products.objects.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'subcategories': subcategories,
        'products': products,
        'p': p,
        'shop': 'active',
    }
    return render(request, 'shop/category.html', context)


def men(request):
    products = Products.objects.filter(category__name="Mens Fashion")
    cart_product_form = CartAddProductForm()
    context = {
        'products': products,
        'cart_product_form': cart_product_form,
        'men': 'active',
    }
    return render(request, 'shop/men.html', context)


def electronic(request):
    products = Products.objects.filter(category__name="Electronics")
    cart_product_form = CartAddProductForm()
    context = {
        'products': products,
        'cart_product_form': cart_product_form,
        'electronic': 'active',
    }
    return render(request, 'shop/electronics.html', context)


# def search(request):
#     q = request.GET.get('q')
#     product = Products.objects.filter(name__icontains=q)
#     context = {
#         'query': q,
#         'product': product,
#         'values': request.GET,
#     }
#     return render(request, 'shop/search.html', context)

def search(request):
    queryset_list = Products.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            queryset_list = queryset_list.filter(name__icontains=q)
    context = {
        'query': q,
        'products': queryset_list,
        'values': request.GET,
    }
    return render(request, 'shop/search.html', context)
