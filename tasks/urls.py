from django.urls import path

from tasks.views import (
    TaskCreateView,
)

urlpatterns = [
    path("create/", TaskCreateView, name="create_task"),
]
