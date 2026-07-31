from django.db import models

from apps.mailer.models import EmailTemplate


class ScheduledCampaign(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("COMPLETED", "Completed"),
    ]

    title = models.CharField(max_length=150)

    template = models.ForeignKey(
        EmailTemplate,
        on_delete=models.CASCADE,
    )

    scheduled_time = models.DateTimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title