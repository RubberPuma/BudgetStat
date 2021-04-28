from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from ..models import Category


class CategoryFactory(DjangoModelFactory):
    category_name = FuzzyChoice(["Food", "Car", "Bills"])

    class Meta:
        model = Category
