from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpRequest
from rest_framework.permissions import IsAuthenticated
from . import models
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from . import serializers

class TodoItemView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request: HttpRequest, pk=None):
        user_todo = get_object_or_404(models.Todo, user=request.user)
        
        if pk:
            todo_item = get_object_or_404(models.TodoItem, id=pk)
            if todo_item.todo.pk is not user_todo.pk:
                return Response({'message' : 'that item does not belong to you'}, status=status.HTTP_403_FORBIDDEN)
            todo_item_serializer = serializers.TodoItemSerializer(instance=todo_item)
            return Response(todo_item_serializer.data, status=status.HTTP_200_OK)
        
        todo_items = models.TodoItem.objects.filter(todo=user_todo)
        todo_items_serializer = serializers.TodoItemSerializer(todo_items, many=True)
        return Response(todo_items_serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request: HttpRequest):
        user_todo = get_object_or_404(models.Todo, user=request.user)
        
        if user_todo is None:
            return Response({'message' : "User's Todo not found"})

        data = request.data.copy()
        data['todo'] = user_todo.pk

        serializer = serializers.TodoItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: HttpRequest, pk):

        user_todo = get_object_or_404(models.Todo, user=request.user)
        todo_item = get_object_or_404(models.TodoItem, id=pk)

        data = request.data.copy()
        if 'todo' in data:
            data.pop('todo')

        if todo_item.todo.pk is not user_todo.pk:
            return Response({'message' : 'that item does not belong to you'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = serializers.TodoItemSerializer(instance=todo_item, data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request: HttpRequest, pk):
        user_todo = get_object_or_404(models.Todo, user=request.user)
        todo_item = get_object_or_404(models.TodoItem, id=pk)

        data = request.data.copy()
        if 'todo' in data:
            data.pop('todo')

        if todo_item.todo.pk is not user_todo.pk:
            return Response({'message' : 'that item does not belong to you'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = serializers.TodoItemSerializer(instance=todo_item, data=data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: HttpRequest, pk):
        user_todo = get_object_or_404(models.Todo, user=request.user)
        todo_item = get_object_or_404(models.TodoItem, id=pk)

        if todo_item.todo.pk is not user_todo.pk:
            return Response({'message' : 'that item does not belong to you'}, status=status.HTTP_403_FORBIDDEN)
        
        todo_item.delete()

        return Response({'message' : 'todo item deleted successfully'}, status=status.HTTP_200_OK)