from django import forms
from .models import Expense
from django.utils import timezone

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["amount", "category", "expense_date", "description", "receipt_details"]
        widgets = {
            "amount": forms.NumberInput(attrs={"class":"form-control", "step":"0.01"}),
            "category": forms.Select(attrs={"class":"form-select"}),
            "expense_date": forms.DateInput(attrs={"type":"date", "class":"form-control"}),
            "description": forms.Textarea(attrs={"class":"form-control", "rows":"3"}),
            "receipt_details": forms.TextInput(attrs={"class":"form-control"}),
        }

    def clean_amount(self):
        amt = self.cleaned_data.get("amount")
        if amt is None or amt <= 0:
            raise forms.ValidationError("Amount must be greater than 0")
        return amt

    def clean_expense_date(self):
        ed = self.cleaned_data.get("expense_date")
        if ed is None:
            raise forms.ValidationError("Enter a valid date")
        if ed > timezone.localdate():
            raise forms.ValidationError("Expense date cannot be in the future")
        return ed

