from django import forms

from apps.mailer.models import EmailTemplate


class SendEmailForm(forms.Form):

    template = forms.ModelChoiceField(
        queryset=EmailTemplate.objects.all(),
        empty_label="Select a Template",
    )