from rest_framework import serializers

from .models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False)

    class Meta:
        model = Expense
        fields = ["description", "amount", "currency", "date", "category"]
