from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Products app home page"""
    return HttpResponse("Products App - iPOS System")
