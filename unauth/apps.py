from django.apps import AppConfig


class UnauthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'unauth'
    
    def ready(self):
        import unauth.signals  # noqa
