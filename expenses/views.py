from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum

@login_required
def dashboard(request):
    if request.user.role == "MANAGER":
        pending_qs = Expense.objects.filter(status=Expense.STATUS_PENDING)
        approved_qs = Expense.objects.filter(status=Expense.STATUS_APPROVED)
        rejected_qs = Expense.objects.filter(status=Expense.STATUS_REJECTED)

        context = {
            "pending_count": pending_qs.count(),
            "approved_count": approved_qs.count(),
            "rejected_count": rejected_qs.count(),

            "total_pending": pending_qs.aggregate(total=Sum("amount"))["total"] or 0,
            "total_approved": approved_qs.aggregate(total=Sum("amount"))["total"] or 0,
            "total_rejected": rejected_qs.aggregate(total=Sum("amount"))["total"] or 0,

            "category_summary": Expense.objects.values("category")
            .annotate(total=Sum("amount"))
            .order_by("category"),
        }

        return render(request, "expenses/manager_dashboard.html", context)

    else:
        recent_expenses = request.user.expenses.order_by("-submitted_date")[:5]
        pending_count = request.user.expenses.filter(status=Expense.STATUS_PENDING).count()
        return render(
            request,
            "expenses/employee_dashboard.html",
            {
                "recent_expenses": recent_expenses,
                "pending_count": pending_count,
            },
        )

@login_required
def expense_create(request):

    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            exp = form.save(commit=False)
            exp.user = request.user
            exp.save()
            return redirect("expenses:history")
    else:
        form = ExpenseForm()
    return render(request, "expenses/expense_create.html", {"form": form})

@login_required
def history(request):
    qs = request.user.expenses.order_by("-submitted_date")
    return render(request, "expenses/history.html", {"expenses": qs})

@login_required
def detail(request, pk):
    exp = get_object_or_404(Expense, pk=pk)
    if request.user != exp.user and request.user.role != "MANAGER":
        return redirect("expenses:dashboard")
    return render(request, "expenses/expense_detail.html", {"expense": exp})

@login_required
def manager_pending(request):
    if request.user.role != "MANAGER":
        return redirect("expenses:dashboard")
    qs = Expense.objects.filter(status=Expense.STATUS_PENDING).order_by("submitted_date")
    return render(request, "expenses/manager_pending.html", {"expenses": qs})

@login_required
def manager_review(request, pk):
    if request.user.role != "MANAGER":
        return redirect("expenses:dashboard")
    exp = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        action = request.POST.get("action")
        comment = request.POST.get("manager_comment", "")
        if action == "approve":
            exp.status = Expense.STATUS_APPROVED
            exp.approved_date = now()
        elif action == "reject":
            exp.status = Expense.STATUS_REJECTED
        exp.manager_comment = comment
        exp.save()
        return redirect("expenses:manager_pending")
    return render(request, "expenses/expense_detail.html", {"expense": exp, "manager_review": True})


@login_required
def manager_report(request):
    if request.user.role != "MANAGER":
        return redirect("expenses:dashboard")

    expenses = Expense.objects.all().order_by("-submitted_date")

    summary = {
        "approved_count": expenses.filter(status=Expense.STATUS_APPROVED).count(),
        "rejected_count": expenses.filter(status=Expense.STATUS_REJECTED).count(),
        "pending_count": expenses.filter(status=Expense.STATUS_PENDING).count(),

        "approved_total": expenses.filter(status=Expense.STATUS_APPROVED).aggregate(
            total=Sum("amount")
        )["total"] or 0,

        "rejected_total": expenses.filter(status=Expense.STATUS_REJECTED).aggregate(
            total=Sum("amount")
        )["total"] or 0,
    }

    return render(
        request,
        "expenses/manager_report.html",
        {
            "expenses": expenses,
            "summary": summary,
        },
    )
