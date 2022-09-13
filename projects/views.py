from django.shortcuts import render
from projects.models import Project
from tasks.models import Task
from django.contrib.auth.decorators import login_required

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
