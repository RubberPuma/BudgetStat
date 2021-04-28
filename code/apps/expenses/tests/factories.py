from datetime import datetime

from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyDate, FuzzyDecimal, FuzzyText

from apps.authentication.tests.factories import UserFactory
from apps.categories.tests.factories import CategoryFactory

from ..consts import CURRENCY_TYPE
from ..models import Expense


class ExpenseFactory(DjangoModelFactory):
    description = FuzzyChoice(["", FuzzyText(length=10)])
    amount = FuzzyDecimal(10, 1000)
    category = SubFactory(CategoryFactory)
    currency = FuzzyChoice([x[0] for x in CURRENCY_TYPE])
    user = SubFactory(UserFactory)
    date = FuzzyDate(
        datetime(2018, 1, 1),
        datetime(2021, 12, 31),
    )

    class Meta:
        model = Expense
