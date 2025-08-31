from django.shortcuts import render
from django.http import HttpResponse
from .models import Report

# Create your views here.

def reports_dashboard(request):
    """Reports dashboard"""
    return HttpResponse("""
    <html>
    <head><title>Reports - iPOS</title></head>
    <body>
        <h1>Reports Dashboard</h1>
        <p>Generate and view business reports.</p>
        <a href="/">← Back to Home</a>
        <ul>
            <li><a href="/reports/sales/">Sales Reports</a></li>
            <li><a href="/reports/inventory/">Inventory Reports</a></li>
            <li><a href="/admin/reports/report/">Admin Panel - Reports</a></li>
        </ul>
    </body>
    </html>
    """)

def sales_report(request):
    """Sales report"""
    return HttpResponse("""
    <html>
    <head><title>Sales Report - iPOS</title></head>
    <body>
        <h1>Sales Report</h1>
        <p>View sales performance and trends.</p>
        <a href="/reports/">← Back to Reports</a>
    </body>
    </html>
    """)

def inventory_report(request):
    """Inventory report"""
    return HttpResponse("""
    <html>
    <head><title>Inventory Report - iPOS</title></head>
    <body>
        <h1>Inventory Report</h1>
        <p>View inventory levels and stock movements.</p>
        <a href="/reports/">← Back to Reports</a>
    </body>
    </html>
    """)
