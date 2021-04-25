from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.forms import BaseInlineFormSet

from apps.expenses.models import Expense
from apps.limits.models import Limit

from .models import User

admin.site.unregister(Group)


class LimitModelFormset(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super(LimitModelFormset, self).__init__(*args, **kwargs)
        _kwargs = {self.fk.name: kwargs["instance"]}
        self.queryset = kwargs["queryset"].filter(**_kwargs).order_by("-id")[:10]


class ExpenseInline(admin.TabularInline):
    verbose_name_plural = "Expenses (last 10)"
    formset = LimitModelFormset
    model = Expense
    extra = 1


class LimitInline(admin.TabularInline):
    verbose_name_plural = "Limits (last 10)"
    formset = LimitModelFormset
    model = Limit
    extra = 1


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ["id", "username", "email"]
    list_display_links = ["id", "username", "email"]
    list_filter = ["is_staff"]
    search_fields = ("username", "email")
    fieldsets = ((("GENERAL"), {"fields": ("username", "email", "password", "is_staff")}),)
    inlines = [
        ExpenseInline,
        LimitInline,
    ]
