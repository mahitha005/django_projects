from django.urls import path
from .views import register_view, logout_view, home_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", logout_view, name="logout"),
    path("", home_view, name="home"),
]