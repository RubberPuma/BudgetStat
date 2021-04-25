from rest_framework import serializers

from .models import Limit


class LimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Limit
        fields = ["limit_value", "current_spent", "period", "start_date", "category", "user"]
