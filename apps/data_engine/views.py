import tempfile
from pathlib import Path

from django.shortcuts import get_object_or_404, redirect, render

from apps.data_engine.importers.csv_importer import CSVImporter
from apps.data_engine.importers.excel_importer import ExcelImporter
from apps.data_engine.models import Recipient
from apps.data_engine.services.recipient_service import RecipientService


def import_recipients(request):

    context = {}

    if request.method == "POST":

        uploaded_file = request.FILES["recipient_file"]

        suffix = Path(uploaded_file.name).suffix

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix
        ) as temp_file:

            for chunk in uploaded_file.chunks():
                temp_file.write(chunk)

            temp_path = temp_file.name

        suffix = Path(uploaded_file.name).suffix.lower()

        if suffix == ".csv":
            df = CSVImporter.load(temp_path)

        elif suffix in [".xlsx", ".xls"]:
            df = ExcelImporter.load(temp_path)

        else:
            raise ValueError("Unsupported file format.")

        created, skipped = RecipientService.save_dataframe(df)

        context["message"] = (
            f"Imported {created} recipients | "
            f"Skipped {skipped}"
        )

    return render(
        request,
        "data_engine/import.html",
        context,
    )



def recipient_list(request):

    recipients = Recipient.objects.all().order_by("name")

    return render(
        request,
        "data_engine/recipients.html",
        {
            "recipients": recipients,
        },
    )


def delete_recipient(request, pk):

    recipient = get_object_or_404(
        Recipient,
        pk=pk,
    )

    if request.method == "POST":

        recipient.delete()

        return redirect("recipient_list")

    return render(
        request,
        "data_engine/delete_recipient.html",
        {
            "recipient": recipient,
        },
    )