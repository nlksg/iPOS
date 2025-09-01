from django import forms
from django.forms import inlineformset_factory
from .models import ProductImage, Variant, Product


class ProductImageUploadForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = [
            'product',
            'variant',
            'image',
            'alt_text',
            'is_primary',
        ]
        widgets = {
            'product': forms.Select(attrs={'data-optional': 'true'}),
        }

    def clean(self):
        cleaned = super().clean()
        product = cleaned.get('product')
        variant = cleaned.get('variant')
        if variant and product and variant.product_id != product.id:
            self.add_error('variant', 'Selected variant does not belong to the chosen product.')
        return cleaned


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'description', 'price', 'sku', 'category', 'is_active'
        ]


VariantFormSet = inlineformset_factory(
    parent_model=Product,
    model=Variant,
    fields=['name', 'price', 'tax_rate', 'barcode', 'stock', 'is_active'],
    extra=0,
    can_delete=True,
)
