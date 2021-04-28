from rest_framework import serializers

from .models import Expense

# from apps.categories.serializers import CategoryRelatedField


class ExpenseSerializer(serializers.ModelSerializer):
    # category = CategoryRelatedField(many=False)

    class Meta:
        model = Expense
        fields = ["description", "amount", "date", "category", "user"]
