import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.authentication.tests.factories import UserFactory
from apps.categories.tests.factories import CategoryFactory
from apps.limits.models import Limit
from apps.limits.serializers import LimitSerializer
from apps.limits.tests.factories import LimitFactory


class LimitTest(APITestCase):
    """ Test module for limits """

    def setUp(self):
        self.category = CategoryFactory()
        self.user1 = UserFactory()
        self.user2 = UserFactory()
        self.limit1 = LimitFactory(user=self.user1, category=self.category)
        self.limit2 = LimitFactory(user=self.user2, category=self.category)
        self.valid_payload = {
            "limit_value": "100",
            "current_spent": "0",
            "period": "M",
            "category": self.category.category_name,
            "start_date": "2021-04-25",
            "user": self.user1.pk,
        }
        self.invalid_payload = {
            "limit_value": "",
        }

    def test_get_all_limits(self):
        # Given
        url = reverse("limit-list")
        limits = Limit.objects.all()
        serializer = LimitSerializer(limits, many=True)

        # When
        response = self.client.get(url)

        # Then
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_limit(self):
        # Given
        url = reverse("limit-detail", kwargs={"pk": self.limit1.pk})
        limit = Limit.objects.get(pk=self.limit1.pk)
        serializer = LimitSerializer(limit)

        # When
        response = self.client.get(url)

        # Then
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_limit(self):
        # Given
        url = reverse("limit-detail", kwargs={"pk": 50})

        # When
        response = self.client.get(url)

        # Then
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_limit(self):
        # Given
        url = reverse("limit-list")

        # When
        response = self.client.post(url, data=json.dumps(self.valid_payload), content_type="application/json")

        # Then
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_limit(self):
        # Given
        url = reverse("limit-list")

        # When
        response = self.client.post(
            url, data=json.dumps(self.invalid_payload), content_type="application/json"
        )

        # Then
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_limit(self):
        # Given
        url = reverse("limit-detail", kwargs={"pk": self.limit1.pk})
        data = json.dumps(self.valid_payload)

        # When
        response = self.client.put(url, data, content_type="application/json")

        # Then
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_limit(self):
        # Given
        url = reverse("limit-detail", kwargs={"pk": self.limit1.pk})
        data = json.dumps(self.invalid_payload)

        # When
        response = self.client.put(url, data, content_type="application/json")

        # Then
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete_limit(self):
        # Given
        url = reverse("limit-detail", kwargs={"pk": self.limit1.pk})

        # When
        response = self.client.delete(url)

        # Then
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_limit(self):
        # Given
        url = reverse("limit-detail", kwargs={"pk": -1})

        # When
        response = self.client.delete(url)

        # Then
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
