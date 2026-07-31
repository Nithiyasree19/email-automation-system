from django.contrib import admin
from django.urls import include, path

urlpatterns = [

    path("", include("apps.dashboard.urls")),

    path("admin/", admin.site.urls),

    path("data/", include("apps.data_engine.urls")),

    path("templates/", include("apps.mailer.urls")),

    path("schedule/", include("apps.automation.urls")),

]