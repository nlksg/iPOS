from django.contrib import admin
from .models import Purchase, PurchaseItem

# Register your models here.

class PurchaseItemInline(admin.TabularInline):
    model = PurchaseItem
    extra = 1

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('purchase_order_number', 'supplier_name', 'total_amount', 'status', 'order_date', 'expected_delivery')
    list_filter = ('status', 'order_date', 'expected_delivery')
    search_fields = ('purchase_order_number', 'supplier_name', 'supplier_contact')
    ordering = ('-order_date',)
    readonly_fields = ('order_date',)
    inlines = [PurchaseItemInline]

@admin.register(PurchaseItem)
class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = ('purchase', 'product', 'quantity_ordered', 'quantity_received', 'unit_cost', 'total_cost')
    list_filter = ('purchase__order_date',)
    search_fields = ('product__name', 'purchase__purchase_order_number')
