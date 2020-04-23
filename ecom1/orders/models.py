from django.db import models
from shop.models import Product


provinces = (('Alberta','Alberta'),('British Columbia','British Columbia'),('Manitoba','Manitoba'),
('New Brunswick','New Brunswick'),('Newfoundland and Labrador','Newfoundland and Labrador'),('Nova Scotia','Nova Scotia'),('Ontario','Ontario'),('Prince Edward Island','Prince Edward Island'),('Quebec','Quebec'),('Saskachewan','Saskachewan'))


class Order(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    contact_number = models.CharField(max_length=30)
    country = models.CharField(max_length=100)
    province = models.CharField(max_length=100 , choices=provinces)
    city = models.CharField(max_length=100)
    unit_no = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity



