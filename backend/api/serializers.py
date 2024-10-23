from rest_framework import serializers
from django.contrib.auth.models import User
from finance.models import Income, Expense

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ["id", "username", "password"]
        extra_kwargs= {"password": {"write_only": True}}
    
    def create(self, validated_data):
        """
        Create a new user with the provided validated data.
            validated_data (dict): A dictionary containing the validated data for the new user.
            User: The newly created user instance.
        """
        user = User.objects.create_user(**validated_data)
        return user

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ["id", "user", "title", "amount", "description", "created_at"]
        extra_kwargs= {"user": {"read_only": True}}

class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = ["id", "user", "title", "amount", "description", "created_at"]
        extra_kwargs = {"user": {"read_only": True}}
