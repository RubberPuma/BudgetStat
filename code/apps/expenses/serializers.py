from rest_framework import serializers

from apps.categories.serializers import CategoryRelatedField

from .models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    category = CategoryRelatedField(many=False)

    class Meta:
        model = Expense
        fields = ["description", "amount", "currency", "date", "category", "user"]
