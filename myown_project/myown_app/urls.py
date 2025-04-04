from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('greetings/',views.greetings,name = 'greetings'),
    path('welcome/', views.welcome, name = 'welcome')
]
