from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm

# Register View
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})

# Logout View
def logout_view(request):
    logout(request)
    return redirect("login")

# Home View (After Login)
def home_view(request):
    return render(request, "accounts/home.html")
