
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def art_club(request):
    return render(request, 'art_club.html')

def music_club(request):
    return render(request, "music_club.html")

def index(request):
    return render(request,'index.html')

def htmlpage(request):
    return render(request, 'htmlpage.html')