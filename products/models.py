from django.db import models

# Create your models here.

class Category(models.Model):
    field_name = models.CharField(max_length=60)
    readable_name = models.CharField(max_length=80)
    description = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.field_name

    def get_readable_name(self):
        return self.readable_name

class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.SET)
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    colours_avail = models.TextField(max_length=254, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024,null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class User(models.Model):
    id = models.CharField(max_length=60, primary_key=True)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=60)
    email_address = models.CharField(max_length=60, null=True, blank=True)
    full_name = models.TextField(max_length=254)
    address = models.TextField(max_length=254, null=True, blank=True)
    contact_no = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.user_name

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    user_id = models.CharField(max_length=60)
    full_name = models.CharField(max_length=254)
    delivery_add = models.TextField(max_length=254)
    status = models.CharField(max_length=30, null=True, blank=True)
    date_created = models.DateField()
    date_updated = models.DateField()
    
    def __str__(self):
        return self.order_id

class Order_item(models.Model):
    order_id = models.ForeignKey('Order', on_delete=models.SET)
    product_id = models.ForeignKey('Product', on_delete=models.SET)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    subtotal = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.order_id