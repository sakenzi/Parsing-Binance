from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
from .management.commands.parsing import start


class TaskConfig(AppConfig):
    name = 'apps.tasks'

    def ready(self):
        start()