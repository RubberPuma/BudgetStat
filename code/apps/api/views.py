from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import CategorySerializer, ExpenseSerializer, LimitSerializer, UserSerializer
from apps.api.models import Category, Expense, Limit
from apps.authentication.models import User

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class LimitViewSet(viewsets.ModelViewSet):
    queryset = Limit.objects.all()
    serializer_class = LimitSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True)
    def expenses(self, request, pk):
        user = self.get_object()
        expenses = Expense.objects.filter(user=user)
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def limits(self, request, pk):
        user = self.get_object()
        limits = Limit.objects.filter(user=user)
        serializer = LimitSerializer(limits, many=True)
        return Response(serializer.data)