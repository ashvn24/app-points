from django.shortcuts import render
from .serializer import CustomUserSerializer, LoginSerializer
from .models import CustomUser
from rest_framework import generics, status
from rest_framework.response import Response
# Create your views here.


class CustomUserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LoginAPIView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context ={'request': request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)