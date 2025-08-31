from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Users app home page"""
    return HttpResponse("Users App - iPOS System")
