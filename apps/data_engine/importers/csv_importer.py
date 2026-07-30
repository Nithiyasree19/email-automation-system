import pandas as pd

from apps.data_engine.mapping.column_mapper import ColumnMapper

REQUIRED_COLUMNS = {"name", "email"}


class CSVImporter:

    @staticmethod
    def load(path):
        df = pd.read_csv(path)

        print("Original Columns:", df.columns.tolist())
        
        df = ColumnMapper.map_columns(df)
        
        print("Mapped Columns:", df.columns.tolist())
        
        df.columns = [
            column.strip().lower()
            for column in df.columns
        ]
        
        print("Normalized Columns:", df.columns.tolist())
        
        missing = REQUIRED_COLUMNS - set(df.columns)

        if missing:
            raise ValueError(
                f"Missing required columns: {', '.join(sorted(missing))}"
            )

        return df