from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def product_list(request):
    """List all products"""
    return HttpResponse("""
    <html>
    <head><title>Products - iPOS</title></head>
    <body>
        <h1>Product Management</h1>
        <p>Manage your product inventory and pricing.</p>
        <a href="/">← Back to Home</a>
        <ul>
            <li><a href="/products/add/">Add New Product</a></li>
            <li><a href="/admin/products/product/">Admin Panel - Products</a></li>
        </ul>
    </body>
    </html>
    """)

def product_add(request):
    """Add new product"""
    return HttpResponse("""
    <html>
    <head><title>Add Product - iPOS</title></head>
    <body>
        <h1>Add New Product</h1>
        <p>Add a new product to the system.</p>
        <a href="/products/">← Back to Products</a>
    </body>
    </html>
    """)

def product_detail(request, pk):
    """Product detail view"""
    return HttpResponse(f"""
    <html>
    <head><title>Product {pk} - iPOS</title></head>
    <body>
        <h1>Product Details</h1>
        <p>Product ID: {pk}</p>
        <a href="/products/">← Back to Products</a>
    </body>
    </html>
    """)
