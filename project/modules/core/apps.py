from django.apps import AppConfig

class CoreConfig(AppConfig):
    name = 'modules.core'
    verbose_name = 'core'
    verbose_name_plural = 'core'

    def ready(self):
        pass