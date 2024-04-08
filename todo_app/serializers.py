from rest_framework import serializers
from . import models
from accounts.serializers import UserSerializer

class TodoSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.Todo
        fields = '__all__'

class TodoItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TodoItem
        fields = '__all__'
        extra_kwargs = {
            'todo': {'required': False, 'write_only' : True} 
        }


