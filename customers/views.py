from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """Customers app index view"""
    return HttpResponse("Customers App - iPOS System")
