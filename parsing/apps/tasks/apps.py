from django.apps import AppConfig


class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.tasks'

    def ready(self):
        from django.conf import settings
        if settings.DEBUG:
            import threading
            from .management.commands.parsing import start
            threading.Thread(target=start).start()
