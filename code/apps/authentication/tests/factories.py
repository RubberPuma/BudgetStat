from factory.django import DjangoModelFactory

from ..models import User


class UserFactory(DjangoModelFactory):
    username = "john"
    email = "lennon@thebeatles.com"
    password = "johnpassword"

    class Meta:
        model = User
