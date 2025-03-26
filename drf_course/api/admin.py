from django.contrib import admin
from .models import User, Color, BaseProduct, Product, Order, OrderItem, Memory
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(BaseProduct)
class BaseProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display = ('memory',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'base_product', 'color', 'stock', 'price', 'in_stock', 'memory')
    list_filter = ('base_product', 'color', 'stock')
    search_fields = ('name', 'base_product__name', 'color__name')
    readonly_fields = ('in_stock',)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    readonly_fields = ('item_subtotal',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'order_id')
    inlines = [OrderItemInline]
    readonly_fields = ('created_at',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'item_subtotal')
    search_fields = ('order__order_id', 'product__name')
    readonly_fields = ('item_subtotal',)
