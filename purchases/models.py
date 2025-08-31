from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

# Create your models here.

class Purchase(models.Model):
    """Purchase order model"""
    purchase_order_number = models.CharField(max_length=50, unique=True)
    supplier_name = models.CharField(max_length=200)
    supplier_contact = models.CharField(max_length=100, blank=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('ordered', 'Ordered'),
        ('received', 'Received'),
        ('cancelled', 'Cancelled'),
    ], default='pending')
    ordered_by = models.ForeignKey(User, on_delete=models.PROTECT)
    order_date = models.DateTimeField(auto_now_add=True)
    expected_delivery = models.DateField(null=True, blank=True)
    received_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"PO {self.purchase_order_number} - {self.supplier_name}"

class PurchaseItem(models.Model):
    """Items in a purchase order"""
    purchase = models.ForeignKey(Purchase, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity_ordered = models.PositiveIntegerField()
    quantity_received = models.PositiveIntegerField(default=0)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    total_cost = models.DecimalField(max_digits=12, decimal_places=2)
    
    def save(self, *args, **kwargs):
        self.total_cost = self.quantity_ordered * self.unit_cost
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.product.name} x {self.quantity_ordered}"
