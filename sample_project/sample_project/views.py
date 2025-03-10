from django.shortcuts import render
from django.http import HttpResponse

def content(request):
    return HttpResponse("Welcome to the Homepage of django!")


# Create your views here.
