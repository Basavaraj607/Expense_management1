from django.contrib import admin
from .models import Expense

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "amount", "category", "expense_date", "status", "submitted_date")
    list_filter = ("status", "category")
    search_fields = ("user__username", "user__email", "description")

admin.site.register(Expense, ExpenseAdmin)
