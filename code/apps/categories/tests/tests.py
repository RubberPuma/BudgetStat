import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.authentication.tests.factories import UserFactory
from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer
from apps.categories.tests.factories import CategoryFactory


class CategoriesTest(APITestCase):
    """ Test module for categories """

    def setUp(self):
        self.user = UserFactory()
        self.food = CategoryFactory(user=self.user)
        self.recreation = CategoryFactory(user=self.user)
        self.bills = CategoryFactory(user=self.user)
        self.car = CategoryFactory(user=self.user)
        self.valid_payload = {
            "category_name": "Name",
            "user": self.user.pk,
        }
        self.invalid_payload = {"category_name": ""}

    def test_get_all_categories(self):
        # Given
        url = reverse("category-list")
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        # When
        response = self.client.get(url)

        # Then
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_category(self):
        # Given
        url = reverse("category-detail", kwargs={"pk": self.food.pk})
        category = Category.objects.get(pk=self.food.pk)
        serializer = CategorySerializer(category)

        # When
        response = self.client.get(url)

        # Then
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_category(self):
        # Given
        url = reverse("category-detail", kwargs={"pk": -1})

        # When
        response = self.client.get(url)

        # Then
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_category(self):
        # Given
        url = reverse("category-list")
        data = json.dumps(self.valid_payload)

        # When
        response = self.client.post(url, data, content_type="application/json")

        # Then
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_category(self):
        # Given
        url = reverse("category-list")
        data = json.dumps(self.invalid_payload)

        # When
        response = self.client.post(url, data, content_type="application/json")

        # Then
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_category(self):
        # Given
        url = reverse("category-detail", kwargs={"pk": self.food.pk})
        data = json.dumps(self.valid_payload)

        # When
        response = self.client.put(url, data, content_type="application/json")

        # Then
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_category(self):
        # Given
        url = reverse("category-detail", kwargs={"pk": self.food.pk})
        data = json.dumps(self.invalid_payload)

        # When
        response = self.client.put(url, data, content_type="application/json")

        # Then
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete_category(self):
        # Given
        url = reverse("category-detail", kwargs={"pk": self.food.pk})

        # When
        response = self.client.delete(url)

        # Then
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_category(self):
        # Given
        url = reverse("category-detail", kwargs={"pk": -1})

        # When
        response = self.client.delete(url)

        # Then
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
