from django.urls import path

from tasks.views import TaskCreateView, TaskListView, TaskUpdateView

urlpatterns = [
    path("create/", TaskCreateView, name="create_task"),
    path("mine/", TaskListView, name="show_my_tasks"),
    path("<int:pk>/complete/", TaskUpdateView.as_view(), name="complete_task"),
]
