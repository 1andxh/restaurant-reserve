from django.urls import path
from core.views import CreateRestaurant, UpdateRestaurant


urlpatterns = [
    path('restaurant/add/', CreateRestaurant.as_view(), name='create-restaurant'),
    path('restaurant/<int:pk>/update/', UpdateRestaurant.as_view(), name='update-restaurant')
]