from django.urls import path
from .views import CreateReservation

urlpatterns = [
    path('restaurants/<int:restaurant_id>/reservation/create/', CreateReservation.as_view(), name='create-reservation')
]