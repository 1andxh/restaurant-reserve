from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from users.serializers import UserSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, status
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
# from rest_framework.authentication import TokenAuthentication

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
#     # queryset = User.objects.get(user=User)
#     serializer_class = UserLoginSerializer
#     permission_classes = [IsAuthenticated]


#     # def login(self, request):
#     #     user = get_object_or_404(User, username=request.data['username'])
#     #     serializer = UserSerializer(instance=user)
#     #     if not user.check_password(request.data['password']):
#     #         return Response({'message': 'username or password is incorrect'}, status=status.HTTP_404_NOT_FOUND)
#     #     token, create = Token.objects.get_or_create(user=user)
#     #     print(f'Token:{token} ')
#     #     return Response({'token': token.key, 'user': serializer.data})
