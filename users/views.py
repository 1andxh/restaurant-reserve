from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from users.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, status
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

User=get_user_model()

class RegisterUser(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            'message': 'User successfully created',
            'user': serializer.data},
            status=status.HTTP_201_CREATED)


# class LoginUser(APIView):
#     queryset = User.objects.get(user=User)
#     serializer_class = UserSerializer

#     def login()