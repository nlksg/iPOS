from django.shortcuts import render
from django.http import HttpResponse
from .models import Account, Transaction

# Create your views here.

def accounts_dashboard(request):
    """Accounts dashboard"""
    return HttpResponse("""
    <html>
    <head><title>Accounts - iPOS</title></head>
    <body>
        <h1>Accounting Dashboard</h1>
        <p>Manage financial accounts and transactions.</p>
        <a href="/">← Back to Home</a>
        <ul>
            <li><a href="/accounts/chart/">Chart of Accounts</a></li>
            <li><a href="/accounts/transactions/">Transactions</a></li>
            <li><a href="/admin/accounts/account/">Admin Panel - Accounts</a></li>
        </ul>
    </body>
    </html>
    """)

def chart_of_accounts(request):
    """Chart of accounts"""
    return HttpResponse("""
    <html>
    <head><title>Chart of Accounts - iPOS</title></head>
    <body>
        <h1>Chart of Accounts</h1>
        <p>Manage your accounting structure.</p>
        <a href="/accounts/">← Back to Accounts</a>
    </body>
    </html>
    """)

def transaction_list(request):
    """Transaction list"""
    return HttpResponse("""
    <html>
    <head><title>Transactions - iPOS</title></head>
    <body>
        <h1>Financial Transactions</h1>
        <p>View and manage financial transactions.</p>
        <a href="/accounts/">← Back to Accounts</a>
    </body>
    </html>
    """)
