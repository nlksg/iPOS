from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """Extended User model for POS system"""
    employee_id = models.CharField(max_length=20, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    role = models.CharField(max_length=20, choices=[
        ('admin', 'Administrator'),
        ('manager', 'Manager'),
        ('cashier', 'Cashier'),
        ('staff', 'Staff'),
    ], default='staff')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.username} ({self.role})"
