from django.db import models

from apps.authentication.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name


class Expense(models.Model):
    CURRENCY_TYPE = [
        ("PLN", "Polish Złoty"),
        ("EUR", "Euro"),
        ("GBP", "British Pound"),
        ("USD", "U.S. Dollar"),
        ("JPY", "Japanese Yen"),
        ("CHF", "Swiss Franc"),
        ("CAD", "Canadian Dollar"),
    ]
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    currency = models.CharField(max_length=3, choices=CURRENCY_TYPE, default="EUR")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.amount} {self.currency} {self.category}"


class Limit(models.Model):
    PERIODS = [
        ("D", "Daily"),
        ("W", "Weekly"),
        ("M", "Monthly"),
        ("Y", "Yearly"),
    ]
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
