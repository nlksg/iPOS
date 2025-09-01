from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, Variant, ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'created_at']
    search_fields = ['name']


class VariantInline(admin.TabularInline):
    model = Variant
    extra = 1
    fields = ['name', 'price', 'tax_rate', 'barcode', 'stock', 'is_active']
    show_change_link = True


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['thumb', 'image', 'alt_text', 'variant', 'is_primary']
    readonly_fields = ['thumb']
    show_change_link = True

    def thumb(self, obj):
        if obj and getattr(obj, 'image', None):
            try:
                return format_html('<img src="{}" style="height:60px;width:auto;border-radius:4px;"/>', obj.image.url)
            except Exception:
                return "(no image)"
        return "(no image)"
    thumb.short_description = "Preview"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['thumbnail', 'name', 'sku', 'price', 'category', 'is_active', 'created_at']
    list_filter = ['category', 'is_active', 'created_at']
    search_fields = ['name', 'sku']
    inlines = [VariantInline, ProductImageInline]

    def thumbnail(self, obj):
        img = getattr(obj, 'get_primary_image', lambda: None)()
        if img and getattr(img, 'image', None):
            try:
                return format_html('<img src="{}" style="height:40px;width:auto;border-radius:4px;"/>', img.image.url)
            except Exception:
                return "-"
        return "-"
    thumbnail.short_description = "Image"
