from django.shortcuts import render
from django.http import HttpResponse

def content(request):
    return HttpResponse("This is content page")