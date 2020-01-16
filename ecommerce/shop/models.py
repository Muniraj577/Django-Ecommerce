from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    category = models.ForeignKey(Category, related_name='subcategory', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category_subcategory', args=[self.slug])


class Products(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING)
    description = models.TextField(max_length=300)
    stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_featured = models.BooleanField(default=False)
    is_latest = models.BooleanField(default=False)
    image = models.ImageField(upload_to='shop/images')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
        # index_together = (('id', 'slug', 'category', 'subcategory'),)

    # def get_absolute_url(self):
    #     return reverse('shop:detail', args=[self.category, self.subcategory, self.slug, self.id])
