from datetime import datetime

from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyDecimal, FuzzyText, FuzzyDate

from apps.categories.tests.factories import CategoryFactory
from apps.authentication.tests.factories import UserFactory

from ..models import Expense


class ExpenseFactory(DjangoModelFactory):
    description = FuzzyChoice(["", FuzzyText(length=10)])
    amount = FuzzyDecimal(10, 1000)
    category = SubFactory(CategoryFactory)
    currency = FuzzyChoice(["PLN", "EUR", "GBP", "USD", "JPY", "CHF", "CAD"])
    user = SubFactory(UserFactory)
    date = FuzzyDate(
        datetime(2018, 1, 1),
        datetime(2021, 12, 31),
    )
    class Meta:
        model = Expense
