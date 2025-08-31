from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """Reports app index view"""
    return HttpResponse("Reports App - iPOS System")
