from django.urls import path
from . import views


appname = 'expenses_manager'
urlpatterns = [
    path("stats", views.stats , name='stats'),

    path("limits", views.limits , name='limits'),
    path("limits/create", views.create_limit , name='create limit'),
    path("limits/<int:pk>/delete", views.DeleteLimit.as_view() , name='delete limit'),
    path("limits/<int:limit_id>/edit", views.edit_limit , name='edit limit'),

    path("expenses/history", views.expenses_history , name='expense history'),
    path("expenses/create", views.create_expense , name='create expense'),
    path("expenses/<int:pk>/delete", views.DeleteExpense.as_view() , name='delete expense'),
    path("expenses/<int:expense_id>/edit", views.edit_expense , name='edit expense'),

    path("expenses/category/create", views.create_category , name='create category'),
    path("expenses/category/<int:pk>/delete", views.DeleteCategory.as_view() , name='delete category'),
    path("expenses/category/<int:category_id/update", views.create_category , name='update category'),
    
]