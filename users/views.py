from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import User

# Create your views here.

def user_list(request):
    """List all users"""
    return HttpResponse("""
    <html>
    <head><title>Users - iPOS</title></head>
    <body>
        <h1>User Management</h1>
        <p>Manage system users and staff members.</p>
        <a href="/">← Back to Home</a>
        <ul>
            <li><a href="/admin/users/user/">Admin Panel - Users</a></li>
        </ul>
    </body>
    </html>
    """)

@login_required
def user_profile(request):
    """User profile page"""
    return HttpResponse(f"""
    <html>
    <head><title>Profile - iPOS</title></head>
    <body>
        <h1>User Profile</h1>
        <p>Welcome, {request.user.username}!</p>
        <a href="/users/">← Back to Users</a>
    </body>
    </html>
    """)
