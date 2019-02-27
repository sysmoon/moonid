from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['token','total', 'emailAddress', 'created', 'billingName', 'billingAddress1', 'billingCity', 'billingPostcode', 'billingCountry', 'shoppingName', 'shoppingAddress1', 'shoppingCity', 'shoppingPostcode', 'shoppingCountry']
admin.site.register(Order,OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'price', 'order']
admin.site.register(OrderItem,OrderItemAdmin)

