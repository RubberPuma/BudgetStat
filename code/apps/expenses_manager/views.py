from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views import generic
from apps.expenses_manager.models import Expense, Category

# display expense history
def history(request):
    return HttpResponse("Expense history subpage")

# display limit management page
def limits(request):
    return HttpResponse("Limits management page")

# display charts suppage 
def charts(request):
    return HttpResponse("Charts subpage")

# display expenes managment page
def manage(request):
    return HttpResponse("Expenses management page")

# display expense create form
def create_expense(request):
    return HttpResponse("Expense create form")

# delete expense
class DeleteExpense(generic.edit.DeleteView):
    success_url = reverse_lazy('manage')
    model = Expense

# display expense update form
def update_expense(request, expense_id):
    return HttpResponse("Expense update form")

# display category create form
def create_category(request):
    return HttpResponse("Category create form")

# delete category and redirect to expenses managment page
class DeleteCategory(generic.edit.DeleteView):
    success_url = reverse_lazy('manage')
    model = Category

# display category update form
def update_category(request, category_id):
    return HttpResponse("Category update form")