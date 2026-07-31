import re


class PlaceholderEngine:

    @staticmethod
    def render(text, recipient):

        data = {
            "name": recipient.name,
            "email": recipient.email,
        }

        data.update(recipient.metadata)

        def replace(match):

            key = match.group(1)

            return str(
                data.get(
                    key,
                    match.group(0),
                )
            )

        return re.sub(
            r"\{(.*?)\}",
            replace,
            text,
        )