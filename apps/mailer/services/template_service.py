from .placeholder_engine import PlaceholderEngine


class TemplateService:

    @staticmethod
    def preview(template, recipient):

        return {
            "subject": PlaceholderEngine.render(
                template.subject,
                recipient,
            ),

            "body": PlaceholderEngine.render(
                template.body,
                recipient,
            ),
        }