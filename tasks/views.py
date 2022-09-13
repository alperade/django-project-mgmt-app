from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm
from tasks.models import Task
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


@login_required
def TaskCreateView(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.save()
            form.save_m2m()
            return redirect("show_project", pk=plan.project.id)
    else:
        form = TaskForm()
    context = {"form": form}
    return render(
        request,
        "tasks/create.html",
        context,
    )


@login_required
def TaskListView(request):
    context = {"tasks": Task.objects.filter(assignee=request.user)}

    return render(request, "tasks/list.html", context)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["is_completed"]
    success_url = reverse_lazy("show_my_tasks")
