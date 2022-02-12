from django.apps import AppConfig


class ProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_Profiles'

    def ready(self):
        import app_Profiles.signals
