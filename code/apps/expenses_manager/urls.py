from django.urls import path
from . import views


appname = 'expenses_manager'
urlpatterns = [
    path("history", views.history , name='history'),
    path("limits", views.limits , name='limits'),

    path("charts", views.charts , name='charts'),

    path("manage", views.manage , name='manage'),
    path("manage/create", views.create_expense , name='create expense'),
    path("manage/<int:pk>/delete", views.DeleteExpense.as_view() , name='delete expense'),
    path("manage/<int:expense_id>/update", views.update_expense , name='update expense'),

    path("category/create", views.create_category , name='create category'),
    path("category/<int:pk>/delete", views.DeleteCategory.as_view() , name='delete category'),
    path("category/<int:category_id/update", views.create_category , name='update category'),
    
]