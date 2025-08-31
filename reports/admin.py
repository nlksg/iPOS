from django.contrib import admin
from .models import Report

# Register your models here.

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('name', 'report_type', 'generated_by', 'date_from', 'date_to', 'generated_at')
    list_filter = ('report_type', 'generated_at', 'date_from')
    search_fields = ('name', 'generated_by__username')
    ordering = ('-generated_at',)
    readonly_fields = ('generated_at',)
