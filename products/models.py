from django.db import models


class Category(models.Model):
    """Product category model"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)

    def get_full_path(self):
        path = [self.name]
        parent = self.parent
        while parent:
            path.insert(0, parent.name)
            parent = parent.parent
        return " > ".join(path)
    
    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.name


class Product(models.Model):
    """Product model for the POS system"""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.sku})"

    def get_primary_image(self):
        """Return primary image if set, otherwise the first image or None."""
        return self.images.filter(is_primary=True).first() or self.images.first()


class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
    name = models.CharField(max_length=120)  # e.g., "Red / L"
    price = models.DecimalField(max_digits=12, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # percent
    barcode = models.CharField(max_length=64, blank=True)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ("product", "name")

    def __str__(self):
        return f"{self.product.name} - {self.name}"

    def get_primary_image(self):
        """Return primary image tied to this variant if any, else None."""
        return self.images.filter(is_primary=True).first() or self.images.first()


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", null=True, blank=True)
    variant = models.ForeignKey('Variant', on_delete=models.SET_NULL, null=True, blank=True, related_name="images")
    image = models.ImageField(upload_to='products/')
    alt_text = models.CharField(max_length=150, blank=True)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        if self.variant:
            return f"{self.product.name} - {self.variant.name} Image"
        return f"{self.product.name} Image"

    class Meta:
        ordering = ['-is_primary', 'id']
