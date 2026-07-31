from django.conf import settings
from django.core.mail import EmailMultiAlternatives


class SMTPService:

    @staticmethod
    def send(subject, body, recipient_email):

        message = EmailMultiAlternatives(
            subject=subject,
            body=body,
            from_email=settings.EMAIL_HOST_USER,
            to=[recipient_email],
        )

        message.send(fail_silently=False)

        return True