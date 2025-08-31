from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Customers app home page"""
    return HttpResponse("Customers App - iPOS System")
