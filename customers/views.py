from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer

# Create your views here.

def customer_list(request):
    """List all customers"""
    return HttpResponse("""
    <html>
    <head><title>Customers - iPOS</title></head>
    <body>
        <h1>Customer Management</h1>
        <p>Manage customer information and relationships.</p>
        <a href="/">← Back to Home</a>
        <ul>
            <li><a href="/customers/add/">Add New Customer</a></li>
            <li><a href="/admin/customers/customer/">Admin Panel - Customers</a></li>
        </ul>
    </body>
    </html>
    """)

def customer_add(request):
    """Add new customer"""
    return HttpResponse("""
    <html>
    <head><title>Add Customer - iPOS</title></head>
    <body>
        <h1>Add New Customer</h1>
        <p>Add a new customer to the system.</p>
        <a href="/customers/">← Back to Customers</a>
    </body>
    </html>
    """)

def customer_detail(request, pk):
    """Customer detail view"""
    return HttpResponse(f"""
    <html>
    <head><title>Customer {pk} - iPOS</title></head>
    <body>
        <h1>Customer Details</h1>
        <p>Customer ID: {pk}</p>
        <a href="/customers/">← Back to Customers</a>
    </body>
    </html>
    """)
