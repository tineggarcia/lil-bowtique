from django.contrib import admin
from .models import Product, Category, User, Order, Order_item

# Register your models here.

class ProductAdmin(admin, ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description',
        'category',
        'price',
        'colours_avail'
        'rating',
        'image',
    )

    ordering= ('sku',)

class CategoryAdmin('admin'.ModelAdmin):
    list_display = (
        'name',
        'field_name',
    )
    
class UserAdmin('admin'.ModelAdmin):
    list_display = (
        'user_name',
        'password', 
        'email_address',
        'full_name',
        'address',
        'contact_no',
    )

class OrderAdmin('admin'.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'delivery_add',
        'status',
        'total',
        'date_created',
    )

class Order_itemAdmin('admin'.MoelAdmin):
    list_display = (
        'order_id',
        'product_id',
        'quantity',
        'subtotal',
    )
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Order_item, Order_itemAdmin)
