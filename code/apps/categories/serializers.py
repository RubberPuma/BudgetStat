from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "category_name", "user"]


class CategoryRelatedField(serializers.RelatedField):
    queryset = Category.objects.all()

    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return Category.objects.get(category_name=data)
