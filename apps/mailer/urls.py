from django.urls import path

from . import views

urlpatterns = [
    path("", views.template_list, name="template_list"),
    path("create/", views.template_create, name="template_create"),
    path("<int:pk>/edit/", views.template_edit, name="template_edit"),
    path("<int:pk>/delete/", views.template_delete, name="template_delete"),
    path("<int:pk>/preview/", views.template_preview, name="template_preview"),
    path("send/", views.send_email, name="send_email"),
    path("test-email/", views.test_email, name="test_email")
]

