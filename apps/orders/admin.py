from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ['game', 'quantity', 'price']
    raw_id_fields = ['game']
    readonly_fields = ['price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_price', 'created']
    list_filter = ['created']
    inlines = [OrderItemInline]
    list_per_page = 20

