from django.urls import path
from . import views


urlpatterns = [
    path("incomes/", views.IncomeList.as_view(), name="income_list"),
    path("incomes/create/", views.IncomeCreate.as_view(), name="income_create"),
    path("incomes/<int:pk>/", views.IncomeDetail.as_view(), name="income_detail"),
    path("expenses/", views.ExpenseList.as_view(), name="expense_list"),
    path("expenses/create/", views.ExpenseCreate.as_view(), name="expense_create"),
    path("expenses/<int:pk>/", views.ExpenseDetail.as_view(), name="expense_detail"),
]
