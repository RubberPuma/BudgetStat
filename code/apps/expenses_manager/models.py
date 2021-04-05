from django.db import models
from apps.authentication.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=50)

class Expense(models.Model):
    CURRENCY_TYPE = [
        ('PLN', 'Polish Złoty'),
        ('EUR', 'Euro'),
        ('GBP', 'British Pound'),
        ('USD', 'U.S. Dollar'),
        ('JPY', 'Japanese Yen'),
        ('CHF', 'Swiss Franc'),
        ('CAD', 'Canadian Dollar'),
    ]
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    currency = models.CharField(max_length=3, choices=CURRENCY_TYPE, default="EUR")
    date = models.DateField()
