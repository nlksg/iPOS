from django.shortcuts import render
from django.http import HttpResponse
from .models import InventoryItem

# Create your views here.

def inventory_list(request):
    """List inventory items"""
    return HttpResponse("""
    <html>
    <head><title>Inventory - iPOS</title></head>
    <body>
        <h1>Inventory Management</h1>
        <p>Track stock levels and inventory status.</p>
        <a href="/">← Back to Home</a>
        <ul>
            <li><a href="/inventory/low-stock/">Low Stock Items</a></li>
            <li><a href="/admin/inventory/inventoryitem/">Admin Panel - Inventory</a></li>
        </ul>
    </body>
    </html>
    """)

def low_stock(request):
    """Show low stock items"""
    return HttpResponse("""
    <html>
    <head><title>Low Stock - iPOS</title></head>
    <body>
        <h1>Low Stock Alert</h1>
        <p>Items that need restocking.</p>
        <a href="/inventory/">← Back to Inventory</a>
    </body>
    </html>
    """)
