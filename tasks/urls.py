from django.urls import path

from tasks.views import TaskCreateView, TaskListView

urlpatterns = [
    path("create/", TaskCreateView, name="create_task"),
    path("mine/", TaskListView, name="show_my_tasks"),
]
