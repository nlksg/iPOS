from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Account(models.Model):
    """Chart of accounts for financial tracking"""
    account_code = models.CharField(max_length=20, unique=True)
    account_name = models.CharField(max_length=200)
    account_type = models.CharField(max_length=20, choices=[
        ('asset', 'Asset'),
        ('liability', 'Liability'),
        ('equity', 'Equity'),
        ('revenue', 'Revenue'),
        ('expense', 'Expense'),
    ])
    parent_account = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.account_code} - {self.account_name}"
    
    class Meta:
        ordering = ['account_code']

class Transaction(models.Model):
    """Financial transaction entries"""
    transaction_date = models.DateField()
    description = models.CharField(max_length=200)
    reference = models.CharField(max_length=50, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.transaction_date} - {self.description}"

class TransactionEntry(models.Model):
    """Individual entries in a transaction (double-entry bookkeeping)"""
    transaction = models.ForeignKey(Transaction, related_name='entries', on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    debit_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    credit_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    description = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return f"{self.account.account_name} - Dr: {self.debit_amount}, Cr: {self.credit_amount}"
