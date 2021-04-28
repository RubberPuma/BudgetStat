from django.db import models

from apps.authentication.models import User
from apps.categories.models import Category

from .consts import PERIODS


class Limit(models.Model):
    limit_value = models.DecimalField(max_digits=15, decimal_places=2)
    current_spent = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    period = models.CharField(max_length=1, choices=PERIODS, default="W")
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    start_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category} {self.limit_value}"

    @property
    def available_funds(self):
        return self.limit_value - self.current_spent
