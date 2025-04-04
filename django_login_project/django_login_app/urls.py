from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django_login_app.views import home_view  # Import from the correct app

urlpatterns = [
    path('', home_view, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),  
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
