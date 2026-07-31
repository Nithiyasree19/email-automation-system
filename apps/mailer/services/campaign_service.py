from apps.data_engine.models import Recipient
from apps.mailer.models import EmailLog
from apps.mailer.services.smtp_service import SMTPService
from apps.mailer.services.template_service import TemplateService


class CampaignService:

    @staticmethod
    def send(template):

        success = 0
        failed = 0

        recipients = Recipient.objects.all()

        for recipient in recipients:

            preview = TemplateService.preview(
                template,
                recipient,
            )

            try:

                SMTPService.send(
                    preview["subject"],
                    preview["body"],
                    recipient.email,
                )

                EmailLog.objects.create(
                    recipient_email=recipient.email,
                    template=template,
                    status="SUCCESS",
                    message="Email sent successfully.",
                )

                success += 1

            except Exception as e:
                print("=" * 60)
                print("EMAIL FAILED")
                print(recipient.email)
                print(type(e).__name__)
                print(str(e))
                print("=" * 60)
            
                EmailLog.objects.create(
                    recipient_email=recipient.email,
                    template=template,
                    status="FAILED",
                    message=str(e),
                )

                failed += 1

        return success, failed