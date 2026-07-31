from django.urls import path

from .views import schedule_campaign

urlpatterns = [

    path("",schedule_campaign,name="schedule_campaign")

]