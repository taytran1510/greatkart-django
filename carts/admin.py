from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.

class CartAmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')

class CartItemAmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')

admin.site.register(Cart, CartAmin)
admin.site.register(CartItem, CartItemAmin)
