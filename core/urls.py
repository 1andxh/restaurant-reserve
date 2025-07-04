from django.urls import path, include
from .views import CreateRestaurant, UpdateRestaurant, ViewRestaurantViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'restaurants',ViewRestaurantViewset )

urlpatterns = [
    path('restaurant/add/', CreateRestaurant.as_view(), name='create-restaurant'),
    path('restaurant/<int:pk>/update/', UpdateRestaurant.as_view(), name='update-restaurant'),
    path('', include(router.urls)),
    
]