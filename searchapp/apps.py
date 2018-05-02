from django.apps import AppConfig


class SearchappConfig(AppConfig):
    name = 'searchapp'

    def ready(self):
        import searchapp.signals
