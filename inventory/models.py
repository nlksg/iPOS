from django.db import models
from products.models import Product


class Inventory(models.Model):
    """Inventory tracking for products"""
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='inventory')
    quantity_on_hand = models.PositiveIntegerField(default=0)
    reorder_level = models.PositiveIntegerField(default=10)
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "inventories"
    
    def __str__(self):
        return f"{self.product.name} - Stock: {self.quantity_on_hand}"
