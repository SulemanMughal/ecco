from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField( blank=True)
    ###############Design Fields ##################
    banner1   = models.BooleanField(default=False)
    banner2   = models.BooleanField(default=False)
    hot_item = models.BooleanField(default=False)
    on_sale  = models.BooleanField(default=False)
    fast_available = models.BooleanField(default=False)
  
    class Meta:
        ordering = ('-updated_at','name' )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


class contact(models.Model):
    Name           =       models.CharField(max_length=100)
    Email          =       models.CharField(max_length=100)
    Subject        =       models.CharField(max_length=100)
    Phone          =       models.CharField(max_length=100)
    Message        =       models.TextField()

    def __str__(self):
        return self.Name