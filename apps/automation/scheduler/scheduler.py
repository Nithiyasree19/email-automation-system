from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone

from apps.automation.services.scheduler_service import SchedulerService

scheduler = BackgroundScheduler(
    timezone=timezone.get_current_timezone()
)


def start_scheduler():

    if not scheduler.running:

        scheduler.add_job(
            SchedulerService.run_pending,
            trigger="interval",
            seconds=30,
            id="run_pending_campaigns",
            replace_existing=True,
        )

        scheduler.start()

        print("✅ APScheduler Started")