from django.shortcuts import render
from projects.models import Project

# from django.contrib.auth.decorators import login_required
# from receipts.forms import ReceiptForm, ExpenseCategoryForm, AccountForm


# username: test_user / test_user2
# password: sifre123


# @login_required
def ProjectListView(request):
    context = {"projects": Project.objects.all()}

    return render(request, "projects/list_projects.html", context)
