from apps.data_engine.models import Recipient
from apps.data_engine.validators.email_validator import is_valid_email


class RecipientService:

    @staticmethod
    def save_dataframe(df):

        created = 0
        skipped = 0

        for _, row in df.iterrows():

            email = str(row["email"]).strip()

            if not is_valid_email(email):
                skipped += 1
                continue

            _, was_created = Recipient.objects.get_or_create(
                email=email,
                defaults={
                    "name": row["name"],
                    "course": row["course"],
                    "due_date": row["due_date"],
                },
            )

            if was_created:
                created += 1
            else:
                skipped += 1

        return created, skipped