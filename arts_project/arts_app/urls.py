
from django.contrib import admin
from django.urls import path, include
from .import views 

urlpatterns = [
    path("", views.index,name ='index'),
    path("art_club/", views.art_club, name = 'art_club'),
    path("music_club/", views.music_club, name = 'music_club'),
    path('htmlpage',views.htmlpage, name = 'htmlpage')
]