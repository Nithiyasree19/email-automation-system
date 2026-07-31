from django.db import models


class EmailTemplate(models.Model):

    name = models.CharField(max_length=150)

    subject = models.CharField(max_length=255)

    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class EmailCampaign(models.Model):

    title = models.CharField(max_length=150)

    template = models.ForeignKey(
        EmailTemplate,
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class EmailLog(models.Model):

    STATUS_CHOICES = [
        ("SUCCESS", "SUCCESS"),
        ("FAILED", "FAILED"),
    ]

    recipient_email = models.EmailField()

    template = models.ForeignKey(
        EmailTemplate,
        on_delete=models.SET_NULL,
        null=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
    )

    message = models.TextField(blank=True)

    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.recipient_email} - {self.status}"