from django.urls import path, re_path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('shop/', views.shop, name='shop'),
    path('men', views.men, name='men'),
    path('electronic', views.electronic, name='electronic'),
    path('<category_slug>', views.shop, name='product_list_by_category'),
    path('products/<category>/<subcategory>', views.products, name='products'),
    path('product/<category>/<subcategory>/<int:id>', views.product_detail, name='detail'),

]
