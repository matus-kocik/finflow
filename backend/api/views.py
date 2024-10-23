from .serializers import UserSerializer, IncomeSerializer, ExpenseSerializer
from django.contrib.auth.models import User
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .permissions import IsAuthenticatedAndOwner
from finance.models import Income, Expense


class UserCreate(CreateAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class IncomeList(ListAPIView):

    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticatedAndOwner]

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)


class IncomeCreate(CreateAPIView):

    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class IncomeDetail(RetrieveUpdateDestroyAPIView):

    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticatedAndOwner]

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)


class ExpenseList(ListAPIView):

    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticatedAndOwner]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)


class ExpenseCreate(CreateAPIView):

    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)
        else:
            print(serializer.errors)


class ExpenseDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticatedAndOwner]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)
