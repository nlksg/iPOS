from django.db import models
from django.conf import settings

# Create your models here.

class Ledger(models.Model):
    """Chart of accounts ledger"""
    ACCOUNT_TYPES = [
        ('asset', 'Asset'),
        ('liability', 'Liability'),
        ('equity', 'Equity'),
        ('revenue', 'Revenue'),
        ('expense', 'Expense'),
    ]
    
    account_number = models.CharField(max_length=20, unique=True)
    account_name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    parent_account = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='sub_accounts')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.account_number} - {self.account_name}"


class JournalEntry(models.Model):
    """Journal entries for double-entry bookkeeping"""
    entry_number = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    reference = models.CharField(max_length=100, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "journal entries"
    
    def __str__(self):
        return f"JE {self.entry_number} - {self.description}"


class Transaction(models.Model):
    """Individual transaction lines within journal entries"""
    TRANSACTION_TYPES = [
        ('debit', 'Debit'),
        ('credit', 'Credit'),
    ]
    
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE, related_name='transactions')
    account = models.ForeignKey(Ledger, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=6, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return f"{self.account.account_name} - {self.get_transaction_type_display()}: ${self.amount}"
