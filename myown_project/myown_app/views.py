from django.shortcuts import render
from django.http import HttpResponse

def greetings(request):
    return HttpResponse("Hello, World")

def welcome(request):
    return HttpResponse("This is content page")
# Create your views here.
