import os

from django.apps import AppConfig


class AutomationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.automation"

    def ready(self):

        if os.environ.get("RUN_MAIN") == "true":

            from apps.automation.scheduler.scheduler import (
                start_scheduler,
            )

            start_scheduler()