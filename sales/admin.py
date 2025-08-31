from django.contrib import admin
from .models import Sale, SaleItem

# Register your models here.

class SaleItemInline(admin.TabularInline):
    model = SaleItem
    extra = 1

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'customer', 'cashier', 'total_amount', 'payment_method', 'status', 'created_at')
    list_filter = ('payment_method', 'status', 'created_at')
    search_fields = ('transaction_id', 'customer__first_name', 'customer__last_name')
    ordering = ('-created_at',)
    readonly_fields = ('transaction_id', 'created_at')
    inlines = [SaleItemInline]

@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = ('sale', 'product', 'quantity', 'unit_price', 'total_price')
    list_filter = ('sale__created_at',)
    search_fields = ('product__name', 'sale__transaction_id')
