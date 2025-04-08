from django.shortcuts import render
from .models import Income, Expense

def view_data(request):
    incomes = Income.objects.all()
    expenses = Expense.objects.all()
    return render(request, "budget/view_data.html", {"incomes": incomes, "expenses": expenses})
