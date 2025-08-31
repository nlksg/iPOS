from django.shortcuts import render
from django.http import HttpResponse
from .models import Purchase

# Create your views here.

def purchase_list(request):
    """List all purchase orders"""
    return HttpResponse("""
    <html>
    <head><title>Purchases - iPOS</title></head>
    <body>
        <h1>Purchase Management</h1>
        <p>Manage purchase orders and supplier relationships.</p>
        <a href="/">← Back to Home</a>
        <ul>
            <li><a href="/purchases/new/">New Purchase Order</a></li>
            <li><a href="/admin/purchases/purchase/">Admin Panel - Purchases</a></li>
        </ul>
    </body>
    </html>
    """)

def new_purchase(request):
    """Create new purchase order"""
    return HttpResponse("""
    <html>
    <head><title>New Purchase - iPOS</title></head>
    <body>
        <h1>New Purchase Order</h1>
        <p>Create a new purchase order.</p>
        <a href="/purchases/">← Back to Purchases</a>
    </body>
    </html>
    """)

def purchase_detail(request, pk):
    """Purchase detail view"""
    return HttpResponse(f"""
    <html>
    <head><title>Purchase {pk} - iPOS</title></head>
    <body>
        <h1>Purchase Order Details</h1>
        <p>Purchase Order ID: {pk}</p>
        <a href="/purchases/">← Back to Purchases</a>
    </body>
    </html>
    """)
