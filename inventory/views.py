from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """Inventory app index view"""
    return HttpResponse("Inventory App - iPOS System")
