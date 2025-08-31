from django.contrib import admin
from .models import InventoryItem

# Register your models here.

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity_on_hand', 'minimum_stock_level', 'maximum_stock_level', 'is_low_stock', 'is_out_of_stock', 'last_restocked')
    list_filter = ('last_restocked', 'location')
    search_fields = ('product__name', 'location')
    ordering = ('product__name',)
    list_editable = ('quantity_on_hand', 'minimum_stock_level', 'maximum_stock_level')
    
    def is_low_stock(self, obj):
        return obj.is_low_stock
    is_low_stock.boolean = True
    is_low_stock.short_description = 'Low Stock'
    
    def is_out_of_stock(self, obj):
        return obj.is_out_of_stock
    is_out_of_stock.boolean = True
    is_out_of_stock.short_description = 'Out of Stock'
