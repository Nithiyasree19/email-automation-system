from django.shortcuts import render

from apps.automation.models import ScheduledCampaign
from apps.data_engine.models import Recipient
from apps.mailer.models import EmailLog, EmailTemplate


def dashboard(request):

    context = {

        "recipient_count": Recipient.objects.count(),

        "template_count": EmailTemplate.objects.count(),

        "scheduled_count": ScheduledCampaign.objects.count(),

        "sent_count": EmailLog.objects.filter(
            status="SUCCESS"
        ).count(),

        "failed_count": EmailLog.objects.filter(
            status="FAILED"
        ).count(),

        "recent_logs": EmailLog.objects.order_by(
            "-sent_at"
        )[:10],

    }

    return render(
        request,
        "dashboard/index.html",
        context,
    )


def email_logs(request):

    status = request.GET.get("status")

    logs = EmailLog.objects.all()

    if status:
        logs = logs.filter(status=status)

    logs = logs.order_by("-sent_at")

    return render(
        request,
        "dashboard/logs.html",
        {
            "logs": logs,
            "status": status,
        },
    )