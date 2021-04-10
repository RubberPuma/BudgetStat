from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views import generic
from apps.expenses_manager.models import Expense, Category, Limit

# display statistics suppage 
def stats(request):
    return HttpResponse("Statistics subpage")

# display limit management page
def limits(request):
    return HttpResponse("Limits management page")

# display limit create form
def create_limit(request):
    return HttpResponse("Limit create form")

# delete limit
class DeleteLimit(generic.edit.DeleteView):
    success_url = reverse_lazy('limits')
    model = Limit

# display limit edit form
def edit_limit(request, expense_id):
    return HttpResponse("Limit edit form")

# display expenses history
def expenses_history(request):
    return HttpResponse("Expenses history subpage")

# display expense create form
def create_expense(request):
    return HttpResponse("Expense create form")

# delete expense
class DeleteExpense(generic.edit.DeleteView):
    success_url = reverse_lazy('manage')
    model = Expense

# display expense edit form
def edit_expense(request, expense_id):
    return HttpResponse("Expense edit form")

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