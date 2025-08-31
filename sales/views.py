from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Sales app home page"""
    return HttpResponse("Sales App - iPOS System")
