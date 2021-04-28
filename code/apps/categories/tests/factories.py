from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from apps.authentication.tests.factories import UserFactory

from ..consts import CATEGORIES
from ..models import Category


class CategoryFactory(DjangoModelFactory):
    category_name = FuzzyChoice(CATEGORIES)
    user = SubFactory(UserFactory)

    class Meta:
        model = Category
