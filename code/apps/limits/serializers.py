from rest_framework import serializers

from .models import Limit


class LimitSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False)

    class Meta:
        model = Limit
        fields = ["limit_value", "current_spent", "period", "start_date", "category"]
