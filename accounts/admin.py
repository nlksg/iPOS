from django.contrib import admin
from .models import Account, Transaction


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['account_number', 'name', 'account_type', 'is_active', 'created_at']
    list_filter = ['account_type', 'is_active']
    search_fields = ['name', 'account_number']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount', 'description', 'transaction_date', 'created_by']
    list_filter = ['transaction_date', 'account__account_type']
    search_fields = ['description', 'account__name']
