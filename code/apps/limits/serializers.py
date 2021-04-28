from rest_framework import serializers

from apps.categories.serializers import CategoryRelatedField

from .models import Limit


class LimitSerializer(serializers.ModelSerializer):
    category = CategoryRelatedField(many=False)

    class Meta:
        model = Limit
        fields = ["limit_value", "current_spent", "period", "start_date", "category", "user"]
