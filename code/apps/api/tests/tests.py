import json

from datetime import datetime

from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status

from apps.api.models import Category, Expense
from apps.api.serializers import CategorySerializer, ExpenseSerializer

from apps.authentication.models import User

client = Client()


class GetAllCategoriesTest(TestCase):
    """ Test module for GET all categories """

    def setUp(self):
        Category.objects.create(category_name="Food")
        Category.objects.create(category_name="Recreation")
        Category.objects.create(category_name="Bills")
        Category.objects.create(category_name="Car")

    def test_get_all_categories(self):
        response = client.get(reverse("category-list"))

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleCategoryTest(TestCase):
    """ Test module for GET single category """

    def setUp(self):
        self.food = Category.objects.create(category_name="Food")
        self.recreation = Category.objects.create(category_name="Recreation")
        self.bills = Category.objects.create(category_name="Bills")
        self.car = Category.objects.create(category_name="Car")

    def test_get_valid_single_category(self):
        response = client.get(reverse("category-detail", kwargs={"pk": self.food.pk}))

        category = Category.objects.get(pk=self.food.pk)
        serializer = CategorySerializer(category)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_category(self):
        response = client.get(reverse("category-detail", kwargs={"pk": 20}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewCategoryTest(TestCase):
    """ Test module for inserting a new category """

    def setUp(self):
        self.valid_payload = {
            "category_name": "Food",
        }
        self.invalid_payload = {
            "category_name": "",
        }

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


class UpdateSingleCategoryTest(TestCase):
    """ Test module for updating an existing category """

    def setUp(self):
        self.food = Category.objects.create(category_name="Foot")
        self.car = Category.objects.create(category_name="Car")
        self.valid_payload = {"category_name": "Food"}
        self.invalid_payload = {"category_name": ""}

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


class DeleteSingleCategoryTest(TestCase):
    """ Test module for deleting an existing category record """

    def setUp(self):
        self.food = Category.objects.create(category_name="Foot")
        self.car = Category.objects.create(category_name="Car")

    def test_valid_delete_category(self):
        response = client.delete(reverse("category-detail", kwargs={"pk": self.food.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_category(self):
        response = client.delete(reverse("category-detail", kwargs={"pk": 20}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class GetAllExpensesTest(TestCase):
    """ Test module for GET all expense """

    def setUp(self):
        category = Category.objects.create(category_name="Food")
        john = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        tom = User.objects.create_user('tom', 'tom@email.com', 'tompassword')
        Expense.objects.create(
            description="",
            amount=50.40,
            category=category,
            currency="EUR",
            user=john,
            date=datetime(2021, 4, 20)
            )
        Expense.objects.create(
            description="",
            amount=69.69,
            category=category,
            currency="EUR",
            user=tom,
            date=datetime(2137, 6, 9)
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
        john = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        tom = User.objects.create_user('tom', 'tom@email.com', 'tompassword')
        self.expense1 = Expense.objects.create(
                            description="",
                            amount=50.40,
                            category=category,
                            currency="EUR",
                            user=john,
                            date=datetime(2021, 4, 20)
                            )
        self.expense2 = Expense.objects.create(
                            description="",
                            amount=69.69,
                            category=category,
                            currency="EUR",
                            user=tom,
                            date=datetime(2137, 6, 9)
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
