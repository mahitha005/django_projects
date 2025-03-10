from django.urls import path
from .views import send_email_view

urlpatterns = [
    path('', send_email_view, name='home'),  # This makes it accessible at "/"
    path('send_email/', send_email_view, name='send_email'),
]
