from django.urls import path

from projects.views import ProjectListView, ProjectDetailView

urlpatterns = [
    path("", ProjectListView, name="list_projects"),
    path("<int:pk>/", ProjectDetailView, name="show_project"),
]
