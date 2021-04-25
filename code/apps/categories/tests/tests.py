import json

from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status

from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer

client = Client()


class CategoriesTest(TestCase):
    """ Test module for categories """

    def setUp(self):
        self.food = Category.objects.create(category_name="Food")
        self.recreation = Category.objects.create(category_name="Recreation")
        self.bills = Category.objects.create(category_name="Bills")
        self.car = Category.objects.create(category_name="Car")
        self.valid_payload = {"category_name": "Food"}
        self.invalid_payload = {"category_name": ""}

    # Test for GET all categories

    def test_get_all_categories(self):
        response = client.get(reverse("category-list"))

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Tests for GET single category

    def test_get_valid_single_category(self):
        response = client.get(reverse("category-detail", kwargs={"pk": self.food.pk}))

        category = Category.objects.get(pk=self.food.pk)
        serializer = CategorySerializer(category)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_category(self):
        response = client.get(reverse("category-detail", kwargs={"pk": 20}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    
    # Tests for inserting a new category

    def test_create_valid_category(self):
        response = client.post(
            reverse("category-list"), data=json.dumps(self.valid_payload), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_category(self):
        response = client.post(
            reverse("category-list"), data=json.dumps(self.invalid_payload), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Tests for updating an existing category

    def test_valid_update_category(self):
        response = client.put(
            reverse("category-detail", kwargs={"pk": self.food.pk}),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_category(self):
        response = client.put(
            reverse("category-detail", kwargs={"pk": self.food.pk}),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Tests for deleting an existing category record

    def test_valid_delete_category(self):
        response = client.delete(reverse("category-detail", kwargs={"pk": self.food.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_category(self):
        response = client.delete(reverse("category-detail", kwargs={"pk": 20}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    
