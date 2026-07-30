from django.core.management.base import BaseCommand

from apps.data_engine.importers.csv_importer import CSVImporter
from apps.data_engine.services.recipient_service import RecipientService


class Command(BaseCommand):

    help = "Import recipients from CSV"

    def add_arguments(self, parser):
        parser.add_argument("file")

    def handle(self, *args, **options):

        df = CSVImporter.load(options["file"])

        created, skipped = RecipientService.save_dataframe(df)

        self.stdout.write(
            self.style.SUCCESS(
                f"Imported: {created} | Skipped: {skipped}"
            )
        )