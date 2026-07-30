from django.urls import path

from .views import import_recipients

urlpatterns = [
    path(
        "import/",
        import_recipients,
        name="import_recipients",
    ),
]