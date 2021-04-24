from django.contrib import admin

from .models import Category, Expense, Limit


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "category_name"]
    list_display_links = ["id", "category_name"]
    ordering = ["id"]
    search_fields = ("category_name__icontains",)


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


@admin.register(Limit)
class LimitAdmin(admin.ModelAdmin):
    list_display = ["user", "limit_value", "available_funds", "period", "category"]
    ordering = ["user"]
    search_fields = ("user__username__icontains", "category__category_name__startswith")
    list_filter = ["user", "category", "period"]
