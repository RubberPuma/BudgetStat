from rest_framework import viewsets
from .serializers import CategorySerializer
from apps.api.models import Category

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

