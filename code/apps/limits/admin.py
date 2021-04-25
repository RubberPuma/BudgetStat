from django.contrib import admin

from .models import Limit


@admin.register(Limit)
class LimitAdmin(admin.ModelAdmin):
    list_display = ["user", "limit_value", "available_funds", "period", "category"]
    ordering = ["user"]
    search_fields = ("user__username__icontains", "category__category_name__startswith")
    list_filter = ["user", "category", "period"]
