from django.db import models
from apps.authentication.models import User

class Account(models.Model):
    CURRENCY_TYPE = [
        ('PLN', 'Polish Złoty'),
        ('EUR', 'Euro'),
        ('GBP', 'British Pound'),
        ('USD', 'U.S. Dollar'),
        ('JPY', 'Japanese Yen'),
        ('CHF', 'Swiss Franc'),
        ('CAD', 'Canadian Dollar'),
    ]
    account_name = models.CharField(max_length=50)
    currency = models.CharField(max_length=3, choices=CURRENCY_TYPE)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Category(models.Model):
    category_name = models.CharField(max_length=50)

class Expense(models.Model):
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateField()
