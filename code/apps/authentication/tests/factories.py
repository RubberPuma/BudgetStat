from factory import Sequence
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText

from ..models import User


class UserFactory(DjangoModelFactory):
    username = FuzzyText(length=10)
    email = Sequence(lambda n: "user%d@email.com" % n)
    password = FuzzyText(length=12)

    class Meta:
        model = User
