from django.contrib import admin
from .models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'cost', 'category', 'barcode', 'is_active', 'created_at')
    list_filter = ('category', 'is_active', 'created_at')
    search_fields = ('name', 'barcode', 'description')
    ordering = ('name',)
    list_editable = ('price', 'is_active')
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'description', 'category', 'barcode')
        }),
        ('Pricing', {
            'fields': ('price', 'cost')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
