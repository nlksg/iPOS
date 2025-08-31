from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Purchases app home page"""
    return HttpResponse("Purchases App - iPOS System")
