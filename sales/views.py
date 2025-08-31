from django.shortcuts import render
from django.http import HttpResponse
from .models import Sale

# Create your views here.

def sales_list(request):
    """List all sales"""
    return HttpResponse("""
    <html>
    <head><title>Sales - iPOS</title></head>
    <body>
        <h1>Sales Management</h1>
        <p>Track and manage sales transactions.</p>
        <a href="/">← Back to Home</a>
        <ul>
            <li><a href="/sales/new/">New Sale</a></li>
            <li><a href="/admin/sales/sale/">Admin Panel - Sales</a></li>
        </ul>
    </body>
    </html>
    """)

def new_sale(request):
    """Create new sale"""
    return HttpResponse("""
    <html>
    <head><title>New Sale - iPOS</title></head>
    <body>
        <h1>New Sale Transaction</h1>
        <p>Create a new sales transaction.</p>
        <a href="/sales/">← Back to Sales</a>
    </body>
    </html>
    """)

def sale_detail(request, pk):
    """Sale detail view"""
    return HttpResponse(f"""
    <html>
    <head><title>Sale {pk} - iPOS</title></head>
    <body>
        <h1>Sale Details</h1>
        <p>Sale ID: {pk}</p>
        <a href="/sales/">← Back to Sales</a>
    </body>
    </html>
    """)
