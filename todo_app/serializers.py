from rest_framework import serializers
from . import models
from accounts.serializers import UserSerializer

class TodoSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.Todo
        fields = '__all__'

class TodoItemSerializer(serializers.ModelSerializer):
    todo = TodoSerializer(required=False)

    class Meta:
        model = models.TodoItem
        fields = '__all__'
