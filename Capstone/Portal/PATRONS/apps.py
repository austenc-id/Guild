from django.apps import AppConfig


class PatronsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PATRONS'

    # def ready(self):
    #     import PATRONS.signals
