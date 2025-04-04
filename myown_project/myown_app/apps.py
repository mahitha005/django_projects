from django.apps import AppConfig


class MyownAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myown_app'
