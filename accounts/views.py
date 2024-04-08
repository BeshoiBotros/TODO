from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpRequest
from . import serializers
from rest_framework.response import Response
from rest_framework import status

class RegisterView(APIView):

    def post(self, request: HttpRequest):
        serializer = serializers.UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
