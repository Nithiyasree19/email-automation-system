from pathlib import Path
import tempfile

from django.shortcuts import render

from apps.data_engine.importers.csv_importer import CSVImporter
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

        df = CSVImporter.load(temp_path)

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