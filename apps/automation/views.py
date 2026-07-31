from datetime import datetime

from django.shortcuts import redirect, render
from django.utils import timezone

from apps.automation.models import ScheduledCampaign
from apps.mailer.models import EmailTemplate


def schedule_campaign(request):

    if request.method == "POST":

        naive_datetime = datetime.strptime(
            request.POST["scheduled_time"],
            "%Y-%m-%dT%H:%M",
        )

        aware_datetime = timezone.make_aware(
            naive_datetime,
            timezone.get_current_timezone(),
        )

        ScheduledCampaign.objects.create(
            title=request.POST["title"],
            template_id=request.POST["template"],
            scheduled_time=aware_datetime,
        )

        return redirect("schedule_campaign")

    templates = EmailTemplate.objects.all()

    campaigns = ScheduledCampaign.objects.order_by(
        "-scheduled_time"
    )

    return render(
        request,
        "automation/schedule.html",
        {
            "templates": templates,
            "campaigns": campaigns,
        },
    )