from django.contrib import admin
from .models import Account, Transaction, TransactionEntry

# Register your models here.

class TransactionEntryInline(admin.TabularInline):
    model = TransactionEntry
    extra = 2

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_code', 'account_name', 'account_type', 'parent_account', 'is_active')
    list_filter = ('account_type', 'is_active')
    search_fields = ('account_code', 'account_name')
    ordering = ('account_code',)
    list_editable = ('is_active',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_date', 'description', 'reference', 'created_by', 'created_at')
    list_filter = ('transaction_date', 'created_at')
    search_fields = ('description', 'reference')
    ordering = ('-transaction_date',)
    readonly_fields = ('created_at',)
    inlines = [TransactionEntryInline]

@admin.register(TransactionEntry)
class TransactionEntryAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'account', 'debit_amount', 'credit_amount', 'description')
    list_filter = ('transaction__transaction_date', 'account__account_type')
    search_fields = ('account__account_name', 'description')
