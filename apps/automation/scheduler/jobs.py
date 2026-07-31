from apps.mailer.models import EmailTemplate
from apps.mailer.services.campaign_service import CampaignService


def send_campaign(template_id):

    try:
        template = EmailTemplate.objects.get(id=template_id)
        CampaignService.send(template)

    except EmailTemplate.DoesNotExist:
        print(f"Template {template_id} not found.")