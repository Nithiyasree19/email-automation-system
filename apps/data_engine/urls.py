from django.urls import path

from .views import (
    delete_recipient,
    import_recipients,
    recipient_list,
)

urlpatterns = [

    path(
        "import/",
        import_recipients,
        name="import_recipients",
    ),

    path(
        "recipients/",
        recipient_list,
        name="recipient_list",
    ),

    path(
        "recipient/<int:pk>/delete/",
        delete_recipient,
        name="delete_recipient",
    ),

]