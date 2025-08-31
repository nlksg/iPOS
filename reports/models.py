from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Report(models.Model):
    """Report generation tracking"""
    name = models.CharField(max_length=200)
    report_type = models.CharField(max_length=50, choices=[
        ('sales', 'Sales Report'),
        ('inventory', 'Inventory Report'),
        ('customer', 'Customer Report'),
        ('financial', 'Financial Report'),
    ])
    generated_by = models.ForeignKey(User, on_delete=models.PROTECT)
    date_from = models.DateField()
    date_to = models.DateField()
    generated_at = models.DateTimeField(auto_now_add=True)
    file_path = models.CharField(max_length=500, blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.report_type}) - {self.generated_at.date()}"
    
    class Meta:
        ordering = ['-generated_at']
