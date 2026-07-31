from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from apps.data_engine.models import Recipient

from .forms import EmailTemplateForm
from .models import EmailTemplate
from .send_forms import SendEmailForm
from .services.campaign_service import CampaignService
from .services.smtp_service import SMTPService
from .services.template_service import TemplateService


def template_list(request):

    templates = EmailTemplate.objects.all()

    return render(
        request,
        "mailer/template_list.html",
        {
            "templates": templates,
        },
    )





def template_create(request):

    if request.method == "POST":

        form = EmailTemplateForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("template_list")

    else:

        form = EmailTemplateForm()

    return render(
        request,
        "mailer/template_form.html",
        {
            "form": form,
        },
    )





def template_edit(request, pk):

    template = get_object_or_404(
        EmailTemplate,
        pk=pk,
    )

    if request.method == "POST":

        form = EmailTemplateForm(
            request.POST,
            instance=template,
        )

        if form.is_valid():

            form.save()

            return redirect("template_list")

    else:

        form = EmailTemplateForm(
            instance=template,
        )

    return render(
        request,
        "mailer/template_form.html",
        {
            "form": form,
        },
    )




def template_delete(request, pk):

    template = get_object_or_404(
        EmailTemplate,
        pk=pk,
    )

    template.delete()

    return redirect("template_list")




def template_preview(request, pk):

    template = get_object_or_404(
        EmailTemplate,
        pk=pk,
    )

    recipient = Recipient.objects.first()

    preview = None

    if recipient:

        preview = TemplateService.preview(
            template,
            recipient,
        )

    return render(
        request,
        "mailer/template_preview.html",
        {
            "template": template,
            "preview": preview,
        },
    )




def send_email(request):

    recipients = Recipient.objects.count()

    if request.method == "POST":

        form = SendEmailForm(request.POST)

        if form.is_valid():

            template = form.cleaned_data["template"]

            success, failed = CampaignService.send(
                template
            )

            return render(
                request,
                "mailer/send_result.html",
                {
                    "success": success,
                    "failed": failed,
                },
            )

    else:

        form = SendEmailForm()

    return render(
        request,
        "mailer/send_email.html",
        {
            "form": form,
            "recipient_count": recipients,
        },
    )



def test_email(request):

    recipient = Recipient.objects.first()

    template = EmailTemplate.objects.first()

    if not recipient or not template:
        return HttpResponse("Create at least one recipient and one template.")

    preview = TemplateService.preview(
        template,
        recipient,
    )

    SMTPService.send(
        preview["subject"],
        preview["body"],
        recipient.email,
    )

    return HttpResponse(
        f"Email sent successfully to {recipient.email}"
    )