from django.db import models

# Create your models here.

class Product(models.Model):
    """Product model for inventory management"""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    barcode = models.CharField(max_length=50, unique=True, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
