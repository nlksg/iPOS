from django.contrib import admin
from .models import Inventory


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity_on_hand', 'reorder_level', 'last_updated']
    list_filter = ['last_updated']
    search_fields = ['product__name']
