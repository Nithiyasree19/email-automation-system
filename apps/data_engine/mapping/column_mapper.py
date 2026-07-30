import re

from .aliases import COLUMN_ALIASES


class ColumnMapper:

    @staticmethod
    def normalize(text):
        """
        Convert variations like:
        Full Name
        Full_Name
        FullName
        FULL-NAME
        -> fullname
        """
        return re.sub(r"[^a-z0-9]", "", str(text).lower())

    @classmethod
    def map_columns(cls, df):

        rename_map = {}

        for column in df.columns:

            normalized_column = cls.normalize(column)

            for target, aliases in COLUMN_ALIASES.items():

                normalized_aliases = [
                    cls.normalize(alias)
                    for alias in aliases
                ]

                if normalized_column in normalized_aliases:
                    rename_map[column] = target
                    break

        return df.rename(columns=rename_map)