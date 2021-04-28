from rest_framework import viewsets

from .models import Limit
from .serializers import LimitSerializer


class LimitViewSet(viewsets.ModelViewSet):
    queryset = Limit.objects.all()
    serializer_class = LimitSerializer
