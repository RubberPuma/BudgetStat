from django.db import models

from apps.authentication.models import User
from apps.categories.models import Category


class Expense(models.Model):
    description = models.CharField(max_length=200, blank=True, default="")
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.amount} {self.currency} {self.category}"
