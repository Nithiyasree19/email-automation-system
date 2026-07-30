import pandas as pd
from pathlib import Path


class CSVImporter:
    REQUIRED_COLUMNS = {"name", "email", "course", "due_date"}

    @staticmethod
    def load(file_path):
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"{path} not found.")

        df = pd.read_csv(path)

        df.columns = [col.strip().lower() for col in df.columns]

        missing = CSVImporter.REQUIRED_COLUMNS - set(df.columns)
        if missing:
            raise ValueError(
                f"Missing required columns: {', '.join(sorted(missing))}"
            )

        return df