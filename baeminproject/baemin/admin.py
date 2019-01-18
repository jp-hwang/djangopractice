from django.contrib import admin
from .models import Shop, Item, Order

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel', 'addr')
    

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('shop', 'name', 'price')
    list_filter = ('shop',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('shop', 'user', 'created_at')
    list_filter = ('shop','user')


