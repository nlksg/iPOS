from django.db import models
from products.models import Product

# Create your models here.

class InventoryItem(models.Model):
    """Inventory tracking for products"""
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='inventory')
    quantity_on_hand = models.PositiveIntegerField(default=0)
    minimum_stock_level = models.PositiveIntegerField(default=10)
    maximum_stock_level = models.PositiveIntegerField(default=100)
    last_restocked = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f"{self.product.name} - Stock: {self.quantity_on_hand}"
    
    @property
    def is_low_stock(self):
        return self.quantity_on_hand <= self.minimum_stock_level
    
    @property
    def is_out_of_stock(self):
        return self.quantity_on_hand == 0
