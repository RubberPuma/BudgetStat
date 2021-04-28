from django.db import models

from apps.authentication.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name
