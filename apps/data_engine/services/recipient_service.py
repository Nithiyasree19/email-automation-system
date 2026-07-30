import math

import pandas as pd

from apps.data_engine.models import Recipient
from apps.data_engine.validators.email_validator import is_valid_email


class RecipientService:

    CORE_FIELDS = {"name", "email"}

    @staticmethod
    def _json_safe(value):
        """
        Convert pandas/numpy values into JSON-safe Python values.
        """

        if pd.isna(value):
            return None

        # Convert numpy scalars to native Python types
        if hasattr(value, "item"):
            value = value.item()

        # Convert Timestamp to string
        if hasattr(value, "isoformat"):
            return value.isoformat()

        # Convert floats like nan/inf
        if isinstance(value, float):
            if math.isnan(value) or math.isinf(value):
                return None

        return value

    @classmethod
    def save_dataframe(cls, df):

        created = 0
        skipped = 0

        for _, row in df.iterrows():

            row_data = row.to_dict()

            email = str(row_data.get("email", "")).strip()

            if not is_valid_email(email):
                skipped += 1
                continue

            name = str(row_data.get("name", "")).strip()

            metadata = {}

            for key, value in row_data.items():

                if key in cls.CORE_FIELDS:
                    continue

                value = cls._json_safe(value)

                if value is None:
                    continue

                metadata[key] = value

            _, was_created = Recipient.objects.get_or_create(
                email=email,
                defaults={
                    "name": name,
                    "metadata": metadata,
                },
            )

            if was_created:
                created += 1
            else:
                skipped += 1

        return created, skipped