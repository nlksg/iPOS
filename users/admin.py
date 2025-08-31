from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Custom user admin"""
    list_display = ['username', 'email', 'first_name', 'last_name', 'phone', 'position', 'is_active']
    list_filter = ['is_active', 'is_staff', 'position']
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('phone', 'position')}),
    )
