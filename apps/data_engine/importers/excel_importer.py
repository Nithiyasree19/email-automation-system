import pandas as pd

from apps.data_engine.mapping.column_mapper import ColumnMapper


REQUIRED_COLUMNS = {"name", "email"}


class ExcelImporter:

    @staticmethod
    def load(path):

        df = pd.read_excel(path)

        df = ColumnMapper.map_columns(df)

        df.columns = [
            str(column).strip().lower()
            for column in df.columns
        ]

        missing = REQUIRED_COLUMNS - set(df.columns)

        if missing:
            raise ValueError(
                f"Missing required columns: {', '.join(sorted(missing))}"
            )

        return df