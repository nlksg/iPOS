from django.contrib import admin
from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['name', 'report_type', 'generated_by', 'date_from', 'date_to', 'created_at']
    list_filter = ['report_type', 'created_at']
    search_fields = ['name']
