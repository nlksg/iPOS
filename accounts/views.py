from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Accounts app home page"""
    return HttpResponse("Accounts App - iPOS System")
