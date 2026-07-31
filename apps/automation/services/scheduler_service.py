from django.utils import timezone

from apps.automation.models import ScheduledCampaign
from apps.mailer.services.campaign_service import CampaignService


class SchedulerService:

    @staticmethod
    def run_pending():

        print(f"[Scheduler] Checking at {timezone.now()}")

        campaigns = ScheduledCampaign.objects.filter(
            status="PENDING",
            scheduled_time__lte=timezone.now(),
        )

        print(f"[Scheduler] Pending campaigns found: {campaigns.count()}")

        for campaign in campaigns:

            print(f"[Scheduler] Sending: {campaign.title}")

            CampaignService.send(campaign.template)

            campaign.status = "COMPLETED"
            campaign.save()

            print(f"[Scheduler] Completed: {campaign.title}")