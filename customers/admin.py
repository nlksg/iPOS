from django.contrib import admin
from .models import Customer

# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at', 'date_of_birth')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    ordering = ('last_name', 'first_name')
    list_editable = ('is_active',)
    
    fieldsets = (
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'date_of_birth')
        }),
        ('Contact Info', {
            'fields': ('email', 'phone_number', 'address')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
