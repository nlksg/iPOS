from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Inventory app home page"""
    return HttpResponse("Inventory App - iPOS System")
