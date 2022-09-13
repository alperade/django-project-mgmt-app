from django.shortcuts import render, redirect
from projects.models import Project
from tasks.models import Task
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm

# username: test_user / test_user2
# password: sifre123


@login_required
def ProjectListView(request):
    context = {"projects": Project.objects.filter(members=request.user)}

    return render(request, "projects/list.html", context)


@login_required
def ProjectDetailView(request, pk):
    context = {
        "projects": Project.objects.filter(members=request.user).get(pk=pk),
        "tasks": Task.objects.filter(assignee=request.user),
    }
    return render(request, "projects/detail.html", context)


@login_required
def ProjectCreateView(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.save()
            form.save_m2m()
            return redirect("show_project", pk=plan.id)
    else:
        form = ProjectForm()
    context = {"form": form}
    return render(
        request,
        "projects/create.html",
        context,
    )
