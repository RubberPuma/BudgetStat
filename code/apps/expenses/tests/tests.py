# import json
from datetime import datetime

from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status

from apps.authentication.models import User
from apps.categories.models import Category
from apps.expenses.models import Expense
from apps.expenses.serializers import ExpenseSerializer

client = Client()


class GetAllExpensesTest(TestCase):
    """ Test module for GET all expense """

    def setUp(self):
        category = Category.objects.create(category_name="Food")
        john = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
        tom = User.objects.create_user("tom", "tom@email.com", "tompassword")
        Expense.objects.create(
            description="",
            amount=50.40,
            category=category,
            currency="EUR",
            user=john,
            date=datetime(2021, 4, 20),
        )
        Expense.objects.create(
            description="",
            amount=69.69,
            category=category,
            currency="EUR",
            user=tom,
            date=datetime(2137, 6, 9),
        )

    def test_get_all_expenses(self):
        response = client.get(reverse("expense-list"))

        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleExpensesTest(TestCase):
    """ Test module for GET single expense """

    def setUp(self):
        category = Category.objects.create(category_name="Food")
        john = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
        tom = User.objects.create_user("tom", "tom@email.com", "tompassword")
        self.expense1 = Expense.objects.create(
            description="",
            amount=50.40,
            category=category,
            currency="EUR",
            user=john,
            date=datetime(2021, 4, 20),
        )
        self.expense2 = Expense.objects.create(
            description="",
            amount=69.69,
            category=category,
            currency="EUR",
            user=tom,
            date=datetime(2137, 6, 9),
        )

    def test_get_valid_single_expense(self):
        response = client.get(reverse("expense-detail", kwargs={"pk": self.expense1.pk}))

        expense = Expense.objects.get(pk=self.expense1.pk)
        serializer = ExpenseSerializer(expense)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_expense(self):
        response = client.get(reverse("expense-detail", kwargs={"pk": 20}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
