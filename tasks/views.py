from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm
from tasks.models import Task


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
