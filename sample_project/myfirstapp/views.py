from django.shortcuts import render
from django.http import HttpResponse
def greetings(request):
    return HttpResponse("Hello, this is django project!")
def entry(request):
    return HttpResponse("Welcome to mydjango App!")


# Create your views here.
