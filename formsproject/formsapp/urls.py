from django.urls import path
from .views import contact_view  # Import the contact view

urlpatterns = [
    path("", contact_view, name="contact"),  # Make contact page the default
    path("contact/", contact_view, name="contact"),
]
