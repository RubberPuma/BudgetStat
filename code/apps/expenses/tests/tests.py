import json
from datetime import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.authentication.tests.factories import UserFactory
from apps.categories.tests.factories import CategoryFactory
from apps.expenses.models import Expense
from apps.expenses.serializers import ExpenseSerializer


class ExpensesTest(APITestCase):
    """ Test module for expenses """

    def setUp(self):
        self.category = CategoryFactory()
        self.john = UserFactory()
        self.tom = UserFactory()
        self.expense1 = Expense.objects.create(
            description="",
            amount=50.40,
            category=self.category,
            currency="EUR",
            user=self.john,
            date=datetime(2021, 4, 20),
        )
        self.expense2 = Expense.objects.create(
            description="",
            amount=69.69,
            category=self.category,
            currency="EUR",
            user=self.tom,
            date=datetime(2137, 6, 9),
        )
        self.valid_payload = {
            "description": "",
            "amount": 69.69,
            "category": self.category.pk,
            "currency": "EUR",
            "user": self.tom.pk,
            "date": "2021-04-25",
        }
        self.invalid_payload = {
            "description": "",
            "amount": "number",
        }

    def test_get_all_expenses(self):
        # Given
        url = reverse("expense-list")
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)

        # When
        response = self.client.get(url)

        # Then
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_expense(self):
        # Given
        url = reverse("expense-detail", kwargs={"pk": self.expense1.pk})
        expense = Expense.objects.get(pk=self.expense1.pk)
        serializer = ExpenseSerializer(expense)

        # When
        response = self.client.get(url)

        # Then
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_expense(self):
        # Given
        url = reverse("expense-detail", kwargs={"pk": 50})

        # When
        response = self.client.get(url)

        # Then
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_expense(self):
        # Given
        url = reverse("expense-list")

        # When
        response = self.client.post(url, data=json.dumps(self.valid_payload), content_type="application/json")

        # Then
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_expense(self):
        # Given
        url = reverse("expense-list")

        # When
        response = self.client.post(
            url, data=json.dumps(self.invalid_payload), content_type="application/json"
        )

        # Then
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_expense(self):
        # Given
        url = reverse("expense-detail", kwargs={"pk": self.expense1.pk})
        data = json.dumps(self.valid_payload)

        # When
        response = self.client.put(url, data, content_type="application/json")

        # Then
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_expense(self):
        # Given
        url = reverse("expense-detail", kwargs={"pk": self.expense1.pk})
        data = json.dumps(self.invalid_payload)

        # When
        response = self.client.put(url, data, content_type="application/json")

        # Then
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete_expense(self):
        # Given
        url = reverse("expense-detail", kwargs={"pk": self.expense1.pk})

        # When
        response = self.client.delete(url)

        # Then
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_expense(self):
        # Given
        url = reverse("expense-detail", kwargs={"pk": -1})

        # When
        response = self.client.delete(url)

        # Then
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
