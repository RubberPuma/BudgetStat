from datetime import datetime

from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyDate, FuzzyDecimal

from apps.authentication.tests.factories import UserFactory
from apps.categories.tests.factories import CategoryFactory

from ..models import Limit

from ..consts import PERIODS

class LimitFactory(DjangoModelFactory):
    limit_value = FuzzyDecimal(500, 1000)
    current_spent = FuzzyDecimal(500)
    period = FuzzyChoice([x[0] for x in PERIODS])
    category = SubFactory(CategoryFactory)
    start_date = FuzzyDate(
        datetime(2018, 1, 1),
        datetime(2021, 12, 31),
    )
    user = SubFactory(UserFactory)

    class Meta:
        model = Limit
