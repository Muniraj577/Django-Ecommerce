from django.contrib import admin
from .models import Products, Category, SubCategory


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'name', 'slug', 'category', 'subcategory', 'price', 'stock', 'image']
    list_filter = ['name', 'category', 'price']
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Products, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubcategoryAdmin)

admin.site.site_header = 'Ecommerce'
admin.site.site_title = 'Ecommerce'