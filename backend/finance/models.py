from django.db import models
from django.contrib.auth.models import User


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, help_text="Income Title")
    amount = models.FloatField(help_text="Income Amount")
    description = models.TextField(help_text="Income Text", blank=True, default="")
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name: str = "Income"
        verbose_name_plural: str = "Incomes"
        ordering: list[str] = ["-created_at"]


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, help_text="Expense Title")
    amount = models.FloatField(help_text="Expense Amount")
    description = models.TextField(help_text="Expense Description", blank=True, default="")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name: str = "Expense"
        verbose_name_plural: str = "Expenses"
        ordering: list[str] = ["-created_at"]
