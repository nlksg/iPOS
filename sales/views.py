from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """Sales app index view"""
    return HttpResponse("Sales App - iPOS System")
