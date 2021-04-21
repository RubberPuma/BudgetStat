from rest_framework import serializers

from apps.api.models import Category, Expense, Limit
from apps.authentication.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "category_name"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]


class ExpenseSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False)

    class Meta:
        model = Expense
        fields = ["description", "amount", "currency", "date", "category"]


class LimitSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False)

    class Meta:
        model = Limit
        fields = ["limit_value", "current_spent", "period", "start_date", "category"]
