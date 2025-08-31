from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """Purchases app index view"""
    return HttpResponse("Purchases App - iPOS System")
