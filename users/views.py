from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """Users app index view"""
    return HttpResponse("Users App - iPOS System")
