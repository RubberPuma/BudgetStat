from rest_framework import serializers

from .models import Limit

# from apps.categories.serializers import CategoryRelatedField


class LimitSerializer(serializers.ModelSerializer):
    # category = CategoryRelatedField(many=False)

    class Meta:
        model = Limit
        fields = ["limit_value", "current_spent", "period", "start_date", "category", "user"]
