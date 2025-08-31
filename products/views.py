from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """Products app index view"""
    return HttpResponse("Products App - iPOS System")
