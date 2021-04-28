from django.contrib import admin

from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ["user", "currency", "amount", "category", "date"]
    list_filter = ["user", "category", "date"]
    list_display_links = ["user", "currency", "category", "date"]
    ordering = ["user"]
    search_fields = (
        "user__username__icontains",
        "category__category_name__icontains",
    )
