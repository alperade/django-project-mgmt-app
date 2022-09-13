from django.urls import path

from projects.views import (
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
)

urlpatterns = [
    path("", ProjectListView, name="list_projects"),
    path("<int:pk>/", ProjectDetailView, name="show_project"),
    path("create/", ProjectCreateView, name="create_project"),
]
