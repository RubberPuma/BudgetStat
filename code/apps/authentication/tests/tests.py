from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.authentication.models import User
from apps.authentication.serializers import UserSerializer
from apps.authentication.tests.factories import UserFactory
from apps.expenses.tests.factories import ExpenseFactory
from apps.expenses.serializers import ExpenseSerializer
from apps.limits.tests.factories import LimitFactory
from apps.limits.serializers import LimitSerializer


class UsersTest(APITestCase):
    """ Test module for users """

    def setUp(self):
        self.user1 = UserFactory()
        self.user2 = UserFactory()
        self.user3 = UserFactory()
        self.limi1 = LimitFactory(user=self.user1)
        self.limi2 = LimitFactory(user=self.user1)
        self.expense1 = ExpenseFactory(user=self.user1)
        self.expense2 = ExpenseFactory(user=self.user1)

    def test_get_all_user_limits(self):
        # Given
        url = reverse("user-limits", kwargs={"pk": self.user1.pk})
        limits = self.user1.limit_set.all()
        serializer = LimitSerializer(limits, many=True)

        # When
        response = self.client.get(url)

        # Then
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_user_expenses(self):
        # Given
        url = reverse("user-expenses", kwargs={"pk": self.user1.pk})
        expenses = self.user1.expense_set.all()
        serializer = ExpenseSerializer(expenses, many=True)

        # When
        response = self.client.get(url)

        # Then
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_users(self):
        # Given
        url = reverse("user-list")
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        # When
        response = self.client.get(url)

        # Then
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_user(self):
        # Given
        url = reverse("user-detail", kwargs={"pk": self.user1.pk})
        users = User.objects.get(pk=self.user1.pk)
        serializer = UserSerializer(users)

        # When
        response = self.client.get(url)

        # Then
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_user(self):
        # Given
        url = reverse("user-detail", kwargs={"pk": -1})

        # When
        response = self.client.get(url)

        # Then
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
