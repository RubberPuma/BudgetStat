from django.contrib import admin

from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "category_name"]
    list_display_links = ["id", "category_name"]
    ordering = ["id"]
    search_fields = ("category_name__icontains",)
