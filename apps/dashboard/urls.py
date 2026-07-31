from django.urls import path

from .views import dashboard, email_logs

urlpatterns = [

    path(
        "",
        dashboard,
        name="dashboard",
    ),

    path(
        "logs/",
        email_logs,
        name="email_logs",
    ),

]