from django.apps import AppConfig


class BitConfig (AppConfig):
    name = 'bit'

    def ready(self):
        import bit.signals
