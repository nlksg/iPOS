from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Reports app home page"""
    return HttpResponse("Reports App - iPOS System")
