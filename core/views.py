from rest_framework import generics, status, viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .serializers import CreateRestaurantSerializer, UpdateRestaurantSerializer, ViewRestaurantSerializer
from .models import Restaurant
from rest_framework.response import Response

class CreateRestaurant(generics.CreateAPIView):
    serializer_class = CreateRestaurantSerializer 
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Restaurant.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        if Restaurant.objects.filter(owner=request.user).exists():
            return Response({
                'error' : 'Restaurant already registered' 
            },
            status=status.HTTP_400_BAD_REQUEST
            )
        return super().create(request, *args, **kwargs)
    
class UpdateRestaurant(generics.UpdateAPIView):
    serializer_class = UpdateRestaurantSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Restaurant.objects.filter(owner=self.request.user)
    
    def perform_update(self, serializer):
    #     serializer.save(owner=self.request.user) -- owner information isn't changing
        serializer.save(owner=self.request.user)


    # def update(self, request, *args, **kwargs):
    #     restaurant = self.get_object()

class ViewRestaurantViewset(viewsets.ModelViewSet):
    serializer_class = ViewRestaurantSerializer
    queryset = Restaurant.objects.all()
    permission_classes = [permissions.AllowAny]